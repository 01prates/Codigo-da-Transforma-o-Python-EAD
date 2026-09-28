import os
import re
import threading
import time
import traceback
import unicodedata
from datetime import datetime

import customtkinter as ctk
from selenium import webdriver
from selenium.common.exceptions import WebDriverException


# ============================================================
# CONFIGURAÇÃO VISUAL
# ============================================================

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")


class StarkIAApp(ctk.CTk):

    def __init__(self):
        super().__init__()

        # ====================================================
        # JANELA
        # ====================================================

        self.title("STARK IA")
        self.geometry("450x650+920+40")
        self.minsize(380, 500)
        self.configure(fg_color="#090D16")

        try:
            self.iconbitmap("stark_logo.ico")
        except Exception:
            pass

        self.attributes("-topmost", True)

        # ====================================================
        # VARIÁVEIS
        # ====================================================

        self.navegador = None
        self.ultimo_cargo = ""
        self.fechando_app = False
        self.busca_em_andamento = False

        self.historico_conversas = []
        self.conversa_atual = []

        self.protocol("WM_DELETE_WINDOW", self.fechar_app)

        # ====================================================
        # LAYOUT PRINCIPAL
        # ====================================================

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.main_chat_frame = ctk.CTkFrame(
            self,
            fg_color="#090D16",
            corner_radius=0
        )

        self.main_chat_frame.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

        # ====================================================
        # HEADER
        # ====================================================

        self.header_frame = ctk.CTkFrame(
            self.main_chat_frame,
            fg_color="#0D1322",
            height=65,
            corner_radius=0
        )

        self.header_frame.pack(
            fill="x",
            side="top"
        )

        self.header_frame.pack_propagate(False)

        self.status_label = ctk.CTkLabel(
            self.header_frame,
            text="● Ativo",
            text_color="#10B981",
            font=("Segoe UI", 11, "bold")
        )

        self.status_label.pack(
            side="right",
            padx=15,
            pady=15
        )

        self.header_label = ctk.CTkLabel(
            self.header_frame,
            text="STARK IA",
            text_color="#F8FAFC",
            font=("Segoe UI", 16, "bold")
        )

        self.header_label.pack(
            side="top",
            pady=18
        )

        # ====================================================
        # CHAT
        # ====================================================

        self.chat_scroll = ctk.CTkScrollableFrame(
            self.main_chat_frame,
            fg_color="#0D1322",
            corner_radius=16,
            border_color="#1E293B",
            border_width=1
        )

        self.chat_scroll.pack(
            pady=15,
            padx=15,
            fill="both",
            expand=True
        )

        # ====================================================
        # INPUT
        # ====================================================

        self.input_frame = ctk.CTkFrame(
            self.main_chat_frame,
            fg_color="transparent"
        )

        self.input_frame.pack(
            fill="x",
            side="bottom",
            pady=15,
            padx=15
        )

        self.entry_msg = ctk.CTkEntry(
            self.input_frame,
            placeholder_text=(
                "Digite cargo e região "
                "(ex: Químico em São Paulo)..."
            ),
            placeholder_text_color="#64748B",
            fg_color="#0D1322",
            text_color="#F8FAFC",
            border_color="#1E293B",
            border_width=1.5,
            height=44,
            corner_radius=22,
            state="normal"
        )

        self.entry_msg.pack(
            side="left",
            fill="x",
            expand=True,
            padx=(0, 8)
        )

        self.entry_msg.bind(
            "<Return>",
            lambda event: self.enviar_mensagem()
        )

        self.btn_enviar = ctk.CTkButton(
            self.input_frame,
            text="➤",
            width=44,
            height=44,
            fg_color="#2563EB",
            text_color="#FFFFFF",
            hover_color="#1D4ED8",
            corner_radius=22,
            font=("Segoe UI", 15, "bold"),
            command=self.enviar_mensagem,
            state="normal"
        )

        self.btn_enviar.pack(side="right")

        # ====================================================
        # MENSAGEM INICIAL
        # ====================================================

        self.adicionar_balao_mensagem(
            "Olá! É um prazer ajudar você hoje. "
            "Como posso auxiliar na sua busca profissional?",
            is_user=False
        )

    # ========================================================
    # LOG
    # ========================================================

    def registrar_erro(self, etapa, erro=None):

        try:
            caminho = os.path.join(
                os.path.expanduser("~"),
                "stark_ia_erro.txt"
            )

            with open(
                caminho,
                "a",
                encoding="utf-8"
            ) as arquivo:

                arquivo.write("\n")
                arquivo.write("=" * 70)
                arquivo.write("\n")

                arquivo.write(
                    f"DATA: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n"
                )

                arquivo.write(
                    f"ETAPA: {etapa}\n"
                )

                if erro is not None:
                    arquivo.write(
                        f"ERRO: {repr(erro)}\n"
                    )

                arquivo.write(
                    traceback.format_exc()
                )

                arquivo.write("\n")

        except Exception:
            pass

    # ========================================================
    # UTILIDADES DE INTERFACE
    # ========================================================

    def executar_na_interface(self, funcao):

        if self.fechando_app:
            return

        try:
            self.after(0, funcao)
        except Exception:
            pass

    def rolar_chat_final(self):

        try:
            self.chat_scroll._parent_canvas.yview_moveto(1.0)
        except Exception:
            pass

    # ========================================================
    # BALÕES
    # ========================================================

    def adicionar_balao_mensagem_direta(
        self,
        texto,
        is_user=False
    ):

        if self.fechando_app:
            return

        msg_container = ctk.CTkFrame(
            self.chat_scroll,
            fg_color="transparent"
        )

        msg_container.pack(
            fill="x",
            pady=6,
            padx=5
        )

        if is_user:

            balao = ctk.CTkFrame(
                msg_container,
                fg_color="#1D4ED8",
                corner_radius=16
            )

            balao.pack(
                side="right",
                anchor="e",
                padx=(45, 0)
            )

            lbl_texto = ctk.CTkLabel(
                balao,
                text=texto,
                font=("Segoe UI", 12),
                text_color="#FFFFFF",
                wraplength=250,
                justify="left"
            )

            lbl_texto.pack(
                anchor="e",
                padx=14,
                pady=10
            )

        else:

            balao = ctk.CTkFrame(
                msg_container,
                fg_color="#161F33",
                corner_radius=16
            )

            balao.pack(
                side="left",
                anchor="w",
                padx=(0, 45)
            )

            lbl_nome = ctk.CTkLabel(
                balao,
                text="STARK IA",
                font=("Segoe UI", 10, "bold"),
                text_color="#10B981"
            )

            lbl_nome.pack(
                anchor="w",
                padx=14,
                pady=(8, 0)
            )

            lbl_texto = ctk.CTkLabel(
                balao,
                text=texto,
                font=("Segoe UI", 12),
                text_color="#F8FAFC",
                wraplength=270,
                justify="left"
            )

            lbl_texto.pack(
                anchor="w",
                padx=14,
                pady=(2, 10)
            )

        self.after(50, self.rolar_chat_final)

        return msg_container

    def adicionar_balao_mensagem(
        self,
        texto,
        is_user=False
    ):

        self.conversa_atual.append(texto)

        return self.adicionar_balao_mensagem_direta(
            texto,
            is_user
        )

    def adicionar_mensagem_thread(
        self,
        texto,
        is_user=False
    ):

        self.executar_na_interface(
            lambda: self.adicionar_balao_mensagem(
                texto,
                is_user
            )
        )

    # ========================================================
    # LOADING
    # ========================================================

    def criar_balao_carregamento(self):

        container = ctk.CTkFrame(
            self.chat_scroll,
            fg_color="transparent"
        )

        container.pack(
            fill="x",
            pady=6,
            padx=5
        )

        balao = ctk.CTkFrame(
            container,
            fg_color="#161F33",
            corner_radius=16
        )

        balao.pack(
            side="left",
            anchor="w",
            padx=(0, 45)
        )

        lbl_nome = ctk.CTkLabel(
            balao,
            text="STARK IA",
            font=("Segoe UI", 10, "bold"),
            text_color="#64748B"
        )

        lbl_nome.pack(
            anchor="w",
            padx=14,
            pady=(8, 0)
        )

        lbl_texto = ctk.CTkLabel(
            balao,
            text="Buscando as melhores oportunidades...",
            font=("Segoe UI", 12, "italic"),
            text_color="#94A3B8"
        )

        lbl_texto.pack(
            anchor="w",
            padx=14,
            pady=(2, 10)
        )

        self.after(50, self.rolar_chat_final)

        return container

    def destruir_loading(self, loading):

        if loading is None:
            return

        def destruir():

            try:
                if loading.winfo_exists():
                    loading.destroy()
            except Exception:
                pass

        self.executar_na_interface(destruir)

    # ========================================================
    # ENVIAR MENSAGEM
    # ========================================================

    def enviar_mensagem(self):

        if self.fechando_app:
            return

        if self.busca_em_andamento:
            return

        texto_usuario = self.entry_msg.get().strip()

        if not texto_usuario:
            return

        self.adicionar_balao_mensagem(
            texto_usuario,
            is_user=True
        )

        self.entry_msg.delete(
            0,
            "end"
        )

        threading.Thread(
            target=self.processar_resposta_ia,
            args=(texto_usuario,),
            daemon=True
        ).start()

    # ========================================================
    # TEXTO
    # ========================================================

    def normalizar_palavra(self, palavra):

        return re.sub(
            r"(.)\1{2,}",
            r"\1",
            palavra
        )

    def remover_acentos(self, texto):

        texto = unicodedata.normalize(
            "NFD",
            texto
        )

        texto = "".join(
            caractere
            for caractere in texto
            if unicodedata.category(caractere) != "Mn"
        )

        return texto

    def transformar_para_url(self, texto):

        texto = texto.lower().strip()

        texto = self.remover_acentos(texto)

        texto = re.sub(
            r"[^a-z0-9\s-]",
            "",
            texto
        )

        texto = re.sub(
            r"\s+",
            "-",
            texto
        )

        texto = re.sub(
            r"-+",
            "-",
            texto
        )

        return texto.strip("-")

    # ========================================================
    # PROCESSAMENTO
    # ========================================================

    def processar_resposta_ia(self, mensagem):

        try:

            msg_raw = mensagem.strip()
            msg_lower = msg_raw.lower()

            time.sleep(0.3)

            # =================================================
            # RESPOSTAS DE CARREIRA
            # =================================================

            if "entrevista" in msg_lower:

                resp = (
                    "Para ir bem em uma entrevista, pesquise "
                    "sobre a empresa com antecedência, treine "
                    "falar sobre suas principais conquistas "
                    "profissionais e demonstre interesse pela vaga."
                )

                self.adicionar_mensagem_thread(resp)
                return

            if (
                "currículo" in msg_lower
                or "curriculo" in msg_lower
                or "perfil" in msg_lower
            ):

                resp = (
                    "Para destacar seu perfil, use verbos de ação "
                    "nas experiências profissionais, destaque "
                    "resultados alcançados e mantenha suas "
                    "competências atualizadas."
                )

                self.adicionar_mensagem_thread(resp)
                return

            if (
                "transição" in msg_lower
                or "transicao" in msg_lower
            ):

                resp = (
                    "Uma transição profissional segura envolve "
                    "mapear suas habilidades atuais, estudar os "
                    "requisitos da nova área e desenvolver "
                    "experiência prática."
                )

                self.adicionar_mensagem_thread(resp)
                return

            if (
                "habilidades" in msg_lower
                or "competências" in msg_lower
                or "competencias" in msg_lower
            ):

                resp = (
                    "O mercado valoriza capacidade de adaptação, "
                    "comunicação, inteligência emocional, resolução "
                    "de problemas e conhecimento tecnológico."
                )

                self.adicionar_mensagem_thread(resp)
                return

            # =================================================
            # ASSUNTOS FORA DO ESCOPO
            # =================================================

            assuntos_proibidos = [
                "receita",
                "bolo",
                "futebol",
                "jogo",
                "fofoca",
                "filme",
                "piada",
                "musica",
                "música",
                "clima",
                "historia",
                "história",
                "politica",
                "política",
                "presidente"
            ]

            if any(
                assunto in msg_lower
                for assunto in assuntos_proibidos
            ):

                resp = (
                    "Desculpe, sou especializada em ajudar "
                    "na busca por vagas de emprego e orientações "
                    "de carreira. Como posso ajudar nessa área?"
                )

                self.adicionar_mensagem_thread(resp)
                return

            # =================================================
            # GATILHOS DE BUSCA
            # =================================================

            gatilhos_busca = [
                "procura",
                "procurar",
                "busca",
                "buscar",
                "vaga",
                "vagas",
                "emprego",
                "quero",
                "preciso",
                "estágio",
                "estagio",
                "trabalhar",
                "trampar"
            ]

            tem_intencao_busca = any(
                gatilho in msg_lower
                for gatilho in gatilhos_busca
            )

            if (
                not tem_intencao_busca
                and not self.ultimo_cargo
                and len(msg_lower.split()) < 2
            ):

                resp = (
                    "Com certeza! Pode me dizer qual cargo "
                    "e região você gostaria de pesquisar?"
                )

                self.adicionar_mensagem_thread(resp)
                return

            # =================================================
            # REGIÕES
            # =================================================

            mapeamento_regioes = {

                "sao paulo": "sao-paulo-sp",
                "são paulo": "sao-paulo-sp",
                "sp": "sao-paulo-sp",

                "rio de janeiro": "rio-de-janeiro-rj",
                "rj": "rio-de-janeiro-rj",

                "belo horizonte": "belo-horizonte-mg",
                "minas gerais": "belo-horizonte-mg",
                "mg": "belo-horizonte-mg",

                "vitoria": "vitoria-es",
                "vitória": "vitoria-es",
                "espirito santo": "vitoria-es",
                "espírito santo": "vitoria-es",
                "es": "vitoria-es",

                "curitiba": "curitiba-pr",
                "parana": "curitiba-pr",
                "paraná": "curitiba-pr",
                "pr": "curitiba-pr",

                "florianopolis": "florianopolis-sc",
                "florianópolis": "florianopolis-sc",
                "santa catarina": "florianopolis-sc",
                "sc": "florianopolis-sc",

                "porto alegre": "porto-alegre-rs",
                "rio grande do sul": "porto-alegre-rs",
                "rs": "porto-alegre-rs",

                "salvador": "salvador-ba",
                "bahia": "salvador-ba",
                "ba": "salvador-ba",

                "recife": "recife-pe",
                "pernambuco": "recife-pe",
                "pe": "recife-pe",

                "fortaleza": "fortaleza-ce",
                "ceara": "fortaleza-ce",
                "ceará": "fortaleza-ce",
                "ce": "fortaleza-ce",

                "sao luis": "sao-luis-ma",
                "são luís": "sao-luis-ma",
                "maranhao": "sao-luis-ma",
                "maranhão": "sao-luis-ma",
                "ma": "sao-luis-ma",

                "natal": "natal-rn",
                "rio grande do norte": "natal-rn",
                "rn": "natal-rn",

                "joao pessoa": "joao-pessoa-pb",
                "joão pessoa": "joao-pessoa-pb",
                "paraiba": "joao-pessoa-pb",
                "paraíba": "joao-pessoa-pb",
                "pb": "joao-pessoa-pb",

                "maceio": "maceio-al",
                "maceió": "maceio-al",
                "alagoas": "maceio-al",
                "al": "maceio-al",

                "aracaju": "aracaju-se",
                "sergipe": "aracaju-se",
                "se": "aracaju-se",

                "teresina": "teresina-pi",
                "piaui": "teresina-pi",
                "piauí": "teresina-pi",
                "pi": "teresina-pi",

                "manaus": "manaus-am",
                "amazonas": "manaus-am",
                "am": "manaus-am",

                "belem": "belem-pa",
                "belém": "belem-pa",
                "para": "belem-pa",
                "pará": "belem-pa",
                "pa": "belem-pa",

                "porto velho": "porto-velho-ro",
                "rondonia": "porto-velho-ro",
                "rondônia": "porto-velho-ro",
                "ro": "porto-velho-ro",

                "rio branco": "rio-branco-ac",
                "acre": "rio-branco-ac",
                "ac": "rio-branco-ac",

                "macapa": "macapa-ap",
                "macapá": "macapa-ap",
                "amapa": "macapa-ap",
                "amapá": "macapa-ap",
                "ap": "macapa-ap",

                "boa vista": "boa-vista-rr",
                "roraima": "boa-vista-rr",
                "rr": "boa-vista-rr",

                "palmas": "palmas-to",
                "tocantins": "palmas-to",
                "to": "palmas-to",

                "brasilia": "brasilia-df",
                "brasília": "brasilia-df",
                "df": "brasilia-df",
                "distrito federal": "brasilia-df",

                "goiania": "goiania-go",
                "goiânia": "goiania-go",
                "goias": "goiania-go",
                "goiás": "goiania-go",
                "go": "goiania-go",

                "cuiaba": "cuiaba-mt",
                "cuiabá": "cuiaba-mt",
                "mato grosso": "cuiaba-mt",
                "mt": "cuiaba-mt",

                "campo grande": "campo-grande-ms",
                "mato grosso do sul": "campo-grande-ms",
                "ms": "campo-grande-ms",

                "campinas": "campinas-sp",
                "santos": "santos-sp",
                "osasco": "osasco-sp",

                "niteroi": "niteroi-rj",
                "niterói": "niteroi-rj",

                "londrina": "londrina-pr",

                "taboao da serra": "taboao-da-serra-sp",
                "taboão da serra": "taboao-da-serra-sp"
            }

            # =================================================
            # ENCONTRAR REGIÃO
            # =================================================

            regiao_encontrada = None
            texto_sem_regiao = msg_lower

            for regiao in sorted(
                mapeamento_regioes.keys(),
                key=len,
                reverse=True
            ):

                padrao = (
                    r"(?:\b(?:em|no|na|de)\s+)?\b("
                    + re.escape(regiao)
                    + r")\b"
                )

                match = re.search(
                    padrao,
                    texto_sem_regiao
                )

                if match:

                    regiao_encontrada = regiao

                    texto_sem_regiao = (
                        texto_sem_regiao[
                            :match.start()
                        ]
                        + " "
                        + texto_sem_regiao[
                            match.end():
                        ]
                    )

                    break

            # =================================================
            # PALAVRAS DESCARTÁVEIS
            # =================================================

            palavras_descartaveis = {

                "ola",
                "olá",
                "oi",
                "eai",
                "salve",
                "suave",
                "fala",
                "hey",
                "opa",
                "mano",
                "cara",
                "velho",

                "bom",
                "dia",
                "boa",
                "tarde",
                "noite",

                "tudo",
                "bem",
                "ta",
                "tá",
                "beleza",
                "blz",
                "ok",
                "okay",

                "entendi",
                "certo",
                "pode",
                "ser",
                "sim",
                "massa",
                "top",
                "show",
                "perfeito",

                "obrigado",
                "obrigada",
                "valeu",
                "vlw",

                "agora",
                "quero",
                "querendo",
                "queria",
                "virar",
                "arrumar",
                "arranja",

                "busco",
                "buscar",
                "procurar",
                "procura",
                "pesquisar",
                "pesquisa",
                "achar",
                "encontrar",

                "preciso",
                "ver",
                "mostra",
                "mostre",
                "tem",
                "consigo",

                "vaga",
                "vagas",
                "emprego",
                "empregos",

                "oportunidade",
                "oportunidades",

                "trampo",
                "trabalhar",
                "trabalho",
                "trampar",

                "para",
                "em",
                "no",
                "na",
                "nos",
                "nas",
                "por",

                "hoje",
                "favor",
                "pfv",
                "porfavor",

                "um",
                "uma",
                "uns",
                "umas",

                "me",
                "mim",
                "pra",
                "pro",

                "ter",
                "como",
                "entao",
                "então",

                "estagio",
                "estágio",

                "empresa"
            }

            cargos_curtos_validos = {
                "ti",
                "rh",
                "ui",
                "ux",
                "pr"
            }

            # =================================================
            # EXTRAÇÃO DO CARGO
            # =================================================

            texto_limpo = re.sub(
                r"[^\w\s]",
                " ",
                texto_sem_regiao
            )

            tokens = texto_limpo.split()

            tokens_normalizados = [
                self.normalizar_palavra(word)
                for word in tokens
            ]

            tokens_cargo = [

                word

                for word in tokens_normalizados

                if (
                    word not in palavras_descartaveis

                    and (
                        len(word) > 2
                        or word in cargos_curtos_validos
                    )
                )
            ]

            cargo_final = " ".join(
                tokens_cargo
            ).strip()

            # =================================================
            # MEMÓRIA DO ÚLTIMO CARGO
            # =================================================

            if (
                not cargo_final
                and self.ultimo_cargo
            ):

                cargo_final = self.ultimo_cargo

            elif cargo_final:

                self.ultimo_cargo = cargo_final

            if not cargo_final:

                resp = (
                    "Por favor, informe qual cargo profissional "
                    "você procura. Exemplo: "
                    "'Analista de dados em São Paulo'."
                )

                self.adicionar_mensagem_thread(resp)
                return

            # =================================================
            # MOSTRAR LOADING
            # =================================================

            self.busca_em_andamento = True

            holder = {
                "loading": None
            }

            evento = threading.Event()

            def criar_loading():

                try:
                    holder["loading"] = (
                        self.criar_balao_carregamento()
                    )
                finally:
                    evento.set()

            self.executar_na_interface(
                criar_loading
            )

            evento.wait(timeout=3)

            # =================================================
            # BUSCAR
            # =================================================

            self.executar_busca_na_pagina(
                cargo_final,
                regiao_encontrada,
                mapeamento_regioes,
                holder["loading"]
            )

        except Exception as erro:

            self.registrar_erro(
                "processar_resposta_ia",
                erro
            )

            self.busca_em_andamento = False

            self.adicionar_mensagem_thread(
                "Ocorreu um problema durante a busca. "
                "O erro foi registrado para diagnóstico."
            )

    # ========================================================
    # CHROME
    # ========================================================

    def navegador_esta_vivo(self):

        if not self.navegador:
            return False

        try:

            return (
                len(
                    self.navegador.window_handles
                ) > 0
            )

        except Exception:
            return False

    def fechar_navegador(self):

        navegador = self.navegador

        self.navegador = None

        if navegador:

            try:
                navegador.quit()
            except Exception:
                pass

    def obter_navegador(self):

        if self.navegador_esta_vivo():
            return self.navegador

        self.fechar_navegador()

        try:

            opcoes = webdriver.ChromeOptions()

            opcoes.add_argument(
                "--disable-blink-features=AutomationControlled"
            )

            opcoes.add_argument(
                "--no-first-run"
            )

            opcoes.add_argument(
                "--no-default-browser-check"
            )

            opcoes.add_argument(
                "--disable-notifications"
            )

            opcoes.add_argument(
                "--disable-popup-blocking"
            )

            opcoes.add_experimental_option(
                "excludeSwitches",
                ["enable-automation"]
            )

            # Selenium Manager localiza/gerencia o driver
            self.navegador = webdriver.Chrome(
                options=opcoes
            )

            self.navegador.set_page_load_timeout(
                30
            )

            try:

                self.navegador.set_window_rect(
                    x=50,
                    y=50,
                    width=950,
                    height=900
                )

            except Exception:
                pass

            return self.navegador

        except Exception as erro:

            self.registrar_erro(
                "obter_navegador",
                erro
            )

            self.navegador = None

            raise

    # ========================================================
    # BUSCA DE VAGAS
    # ========================================================

    def executar_busca_na_pagina(
        self,
        cargo,
        regiao_chave,
        mapeamento_regioes,
        balao_loading
    ):

        try:

            navegador = self.obter_navegador()

            # -----------------------------------------------
            # TRANSFORMA O CARGO PARA URL
            # -----------------------------------------------

            cargo_url = self.transformar_para_url(
                cargo
            )

            if not cargo_url:
                raise ValueError(
                    "Não foi possível gerar a URL do cargo."
                )

            # -----------------------------------------------
            # URL
            # -----------------------------------------------

            if regiao_chave:

                regiao_url = (
                    mapeamento_regioes.get(
                        regiao_chave
                    )
                )

                if not regiao_url:

                    regiao_url = (
                        self.transformar_para_url(
                            regiao_chave
                        )
                    )

                url_busca = (
                    "https://www.catho.com.br/vagas/"
                    f"{cargo_url}/"
                    f"{regiao_url}/"
                )

            else:

                url_busca = (
                    "https://www.catho.com.br/vagas/"
                    f"{cargo_url}/"
                )

            # -----------------------------------------------
            # DEBUG
            # -----------------------------------------------

            print(
                f"[STARK IA] Abrindo: {url_busca}"
            )

            # -----------------------------------------------
            # ABRIR
            # -----------------------------------------------

            navegador.get(
                url_busca
            )

            time.sleep(2)

            # -----------------------------------------------
            # COOKIES
            # -----------------------------------------------

            self.aceitar_cookies()

            # -----------------------------------------------
            # REMOVE LOADING
            # -----------------------------------------------

            self.destruir_loading(
                balao_loading
            )

            # -----------------------------------------------
            # RESPOSTA
            # -----------------------------------------------

            if regiao_chave:

                mensagem = (
                    f"Prontinho! Pesquisei vagas de "
                    f"'{cargo.title()}' em "
                    f"{regiao_chave.title()} e deixei "
                    f"os resultados abertos no navegador."
                )

            else:

                mensagem = (
                    f"Prontinho! Pesquisei vagas para "
                    f"'{cargo.title()}' e deixei "
                    f"os resultados abertos no navegador."
                )

            self.adicionar_mensagem_thread(
                mensagem
            )

        except WebDriverException as erro:

            self.registrar_erro(
                "Selenium / Chrome WebDriver",
                erro
            )

            self.destruir_loading(
                balao_loading
            )

            self.adicionar_mensagem_thread(
                "Não consegui iniciar ou controlar o Chrome. "
                "O erro foi salvo em stark_ia_erro.txt."
            )

            self.fechar_navegador()

        except Exception as erro:

            self.registrar_erro(
                "executar_busca_na_pagina",
                erro
            )

            self.destruir_loading(
                balao_loading
            )

            self.adicionar_mensagem_thread(
                "Tive um problema ao abrir as vagas. "
                "O erro foi salvo em stark_ia_erro.txt."
            )

            self.fechar_navegador()

        finally:

            self.busca_em_andamento = False

    # ========================================================
    # COOKIES
    # ========================================================

    def aceitar_cookies(self):

        if not self.navegador:
            return

        try:

            time.sleep(1)

            self.navegador.execute_script(
                """
                const botoes = document.querySelectorAll(
                    "button"
                );

                for (const btn of botoes) {

                    const texto = (
                        btn.innerText || ""
                    ).toLowerCase();

                    if (
                        texto.includes("aceitar") ||
                        texto.includes("permitir") ||
                        texto.includes("concordar")
                    ) {

                        btn.click();
                        break;
                    }
                }
                """
            )

        except Exception:
            # Cookie é opcional, então não derruba a busca
            pass

    # ========================================================
    # FECHAR APP
    # ========================================================

    def fechar_app(self):

        if self.fechando_app:
            return

        self.fechando_app = True

        try:

            self.fechar_navegador()

        except Exception:
            pass

        try:
            self.destroy()
        except Exception:
            pass


# ============================================================
# INICIAR
# ============================================================

if __name__ == "__main__":

    app = StarkIAApp()

    app.mainloop()
