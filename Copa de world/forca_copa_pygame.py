"""
⚽  FORCA DA COPA DO MUNDO 2026  ⚽
Pygame Edition — André
"""

import pygame
import sys
import random
import math
import time

# ══════════════════════════════════════════════
#  INICIALIZAÇÃO
# ══════════════════════════════════════════════
pygame.init()

W, H = 1100, 720
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("⚽ Forca da Copa do Mundo 2026")
clock = pygame.time.Clock()
FPS = 60

# ══════════════════════════════════════════════
#  PALETA — Verde gramado + dourado troféu
# ══════════════════════════════════════════════
C = {
    "bg":        (10,  20,  15),   # verde noite profundo
    "field":     (22,  60,  36),   # gramado escuro
    "field2":    (18,  48,  28),   # listras alternadas
    "panel":     (14,  30,  20),   # painel lateral
    "gold":      (255, 210,  50),  # dourado troféu
    "gold2":     (200, 155,  20),  # dourado escuro
    "white":     (245, 245, 235),  # branco quente
    "gray":      (130, 145, 135),  # cinza neutro
    "red":       (220,  50,  50),  # erro / perigo
    "green":     ( 80, 200,  90),  # acerto
    "blue":      ( 70, 140, 220),  # info
    "line":      ( 40,  80,  55),  # linhas do campo
    "letter_bg": ( 25,  55,  35),  # fundo letras
    "win_bg":    ( 10,  60,  30),  # vitória
    "lose_bg":   ( 60,  10,  15),  # derrota
    "btn":       ( 30,  80,  50),
    "btn_hover": ( 50, 120,  70),
    "btn_sel":   (180, 140,  10),
}

# ══════════════════════════════════════════════
#  FONTES
# ══════════════════════════════════════════════
def load_font(name, size, bold=False):
    try:
        return pygame.font.SysFont(name, size, bold=bold)
    except:
        return pygame.font.Font(None, size)

F = {
    "title":  load_font("poppins",       72, bold=True),
    "sub":    load_font("poppins",       28, bold=True),
    "body":   load_font("liberationsans",22),
    "word":   load_font("dejavusans",    46, bold=True),
    "letter": load_font("dejavusans",    30, bold=True),
    "small":  load_font("liberationsans",17),
    "tiny":   load_font("liberationsans",14),
    "score":  load_font("poppins",       36, bold=True),
    "hint":   load_font("liberationsans",19),
    "btn":    load_font("poppins",       22, bold=True),
    "cat":    load_font("poppins",       16, bold=True),
    "stage_title": load_font("poppins",  52, bold=True),
}

# ══════════════════════════════════════════════
#  BANCO DE PERGUNTAS
# ══════════════════════════════════════════════
PERGUNTAS = {
    "facil": [
        {"palavra": "PELÉ",      "dica": "Maior artilheiro da história da Seleção, tricampeão mundial",                 "cat": "🇧🇷 Lenda do Brasil"},
        {"palavra": "BRASIL",    "dica": "País com mais títulos mundiais — cinco conquistas",                            "cat": "🏆 Campeões"},
        {"palavra": "MESSI",     "dica": "Campeão mundial com a Argentina em 2022 e Bola de Ouro do torneio",           "cat": "⚽ Ídolos"},
        {"palavra": "MARACANAZO","dica": "Derrota do Brasil para o Uruguai em 1950 no próprio Maracanã",                "cat": "📜 História"},
        {"palavra": "NEYMAR",    "dica": "Atacante brasileiro que disputou as Copas de 2014 e 2022",                    "cat": "🇧🇷 Seleção"},
        {"palavra": "ARGENTINA", "dica": "Campeã mundial em 2022, no Qatar",                                            "cat": "🏆 Campeões"},
        {"palavra": "MBAPPE",    "dica": "Artilheiro da final de 2022 e capitão da França",                             "cat": "⚽ Ídolos"},
        {"palavra": "ALEMANHA",  "dica": "País que aplicou o 7x1 no Brasil em 2014",                                    "cat": "📜 História"},
        {"palavra": "QATAR",     "dica": "País-sede da Copa do Mundo de 2022",                                          "cat": "🌍 Sedes"},
        {"palavra": "RONALDO",   "dica": "R9 — artilheiro histórico das Copas com 15 gols, campeão em 94 e 2002",      "cat": "🇧🇷 Lenda do Brasil"},
        {"palavra": "ITALIA",    "dica": "País com 4 títulos mundiais, não se classificou para 2022 nem 2026",          "cat": "📜 História"},
        {"palavra": "FRANCA",    "dica": "Campeã em 1998 e 2018, finalista em 2022",                                    "cat": "🏆 Campeões"},
        {"palavra": "MEXICO",    "dica": "Coorganizador da Copa 2026 e anfitriões em 1970 e 1986",                      "cat": "🌍 Sedes"},
        {"palavra": "CANADA",    "dica": "País norte-americano que coorganiza a Copa 2026 pela primeira vez",           "cat": "🎯 Copa 2026"},
        {"palavra": "PORTUGAL",  "dica": "Seleção europeia liderada por Cristiano Ronaldo",                             "cat": "⚽ Ídolos"},
    ],
    "medio": [
        {"palavra": "VINICIUS JUNIOR",  "dica": "Atacante do Real Madrid, principal esperança do Brasil na Copa 2026",     "cat": "🇧🇷 Seleção"},
        {"palavra": "LAMINE YAMAL",     "dica": "Joia espanhola nascida em 2007, destaque na Eurocopa 2024",               "cat": "🎯 Copa 2026"},
        {"palavra": "HAALAND",          "dica": "Artilheiro norueguês da Premier League, favorito a artilheiro em 2026",   "cat": "🎯 Copa 2026"},
        {"palavra": "BELLINGHAM",       "dica": "Meio-campista inglês do Real Madrid, esperança da Inglaterra em 2026",    "cat": "🎯 Copa 2026"},
        {"palavra": "ZIDANE",           "dica": "Francês que cabeceou na final de 2006 e foi expulso — campeão em 98",    "cat": "⚽ Ídolos"},
        {"palavra": "MARADONA",         "dica": "Campeão em 1986, autor do gol A Mão de Deus contra a Inglaterra",        "cat": "⚽ Ídolos"},
        {"palavra": "EUSEBIO",          "dica": "Artilheiro de Portugal na Copa de 1966, com 9 gols — 3° lugar",          "cat": "📜 História"},
        {"palavra": "ESTADOS UNIDOS",   "dica": "País que sediará a maioria das partidas da Copa 2026",                    "cat": "🎯 Copa 2026"},
        {"palavra": "METLIFE STADIUM",  "dica": "Estádio em Nova Jersey onde será a final da Copa 2026",                  "cat": "🎯 Copa 2026"},
        {"palavra": "PEDRI",            "dica": "Meio-campista espanhol do Barcelona, herdeiro do estilo de Xavi",         "cat": "🎯 Copa 2026"},
        {"palavra": "RODRIGO DE PAUL",  "dica": "Meio-campo titular da Argentina campeã em 2022",                          "cat": "⚽ Ídolos"},
        {"palavra": "RODRYGO",          "dica": "Atacante brasileiro do Real Madrid, reserva de luxo na Copa 2026",        "cat": "🇧🇷 Seleção"},
        {"palavra": "BOLA DE OURO",     "dica": "Prêmio ao melhor jogador de cada edição da Copa do Mundo",               "cat": "🏆 Prêmios"},
        {"palavra": "GUARDIOLA",        "dica": "Técnico do Manchester City, ex-jogador e ídolo do Barcelona",             "cat": "⚽ Ídolos"},
        {"palavra": "ENDRICK",          "dica": "Atacante brasileiro do Real Madrid, nascido em 2006",                     "cat": "🇧🇷 Seleção"},
    ],
    "dificil": [
        {"palavra": "JUST FONTAINE",      "dica": "Francês que marcou 13 gols em uma Copa (1958) — recorde histórico",        "cat": "📜 História"},
        {"palavra": "ESTADIO AZTECA",     "dica": "Único estádio a receber três Copas do Mundo: 1970, 1986 e 2026",           "cat": "🌍 Sedes"},
        {"palavra": "SANDOR KOCSIS",      "dica": "Húngaro com 11 gols na Copa de 1954 — vice-artilheiro histórico",          "cat": "📜 História"},
        {"palavra": "LOTHAR MATTHAUS",    "dica": "Alemão que jogou 5 Copas do Mundo — recorde masculino",                    "cat": "📜 História"},
        {"palavra": "JOSIMAR",            "dica": "Lateral brasileiro que marcou dois gols antológicos na Copa de 1986",       "cat": "🇧🇷 Lenda do Brasil"},
        {"palavra": "ALEJANDRO GARNACHO", "dica": "Atacante argentino do Manchester United — geração pós-Messi em 2026",      "cat": "🎯 Copa 2026"},
        {"palavra": "DIOGO JOTA",         "dica": "Atacante de Portugal do Liverpool, titular ao lado de Bruno Fernandes",    "cat": "🎯 Copa 2026"},
        {"palavra": "ANTONEE ROBINSON",   "dica": "Lateral esquerdo da seleção dos EUA, um dos anfitriões da Copa 2026",     "cat": "🎯 Copa 2026"},
        {"palavra": "SEATTLE",            "dica": "Cidade americana no noroeste que sediará partidas da Copa 2026",           "cat": "🌍 Sedes"},
        {"palavra": "FRITZ WALTER",       "dica": "Capitão da Alemanha Ocidental campeã em 1954, derrotando a Hungria",       "cat": "📜 História"},
        {"palavra": "GIGI BUFFON",        "dica": "Goleiro italiano campeão em 2006, disputou 5 Copas do Mundo",             "cat": "⚽ Ídolos"},
        {"palavra": "KANSAS CITY",        "dica": "Cidade americana que sediará partidas da Copa 2026 no Arrowhead Stadium",  "cat": "🎯 Copa 2026"},
        {"palavra": "NICO WILLIAMS",      "dica": "Atacante espanhol, irmão de Inaki Williams, destaque da Eurocopa 2024",   "cat": "🎯 Copa 2026"},
        {"palavra": "CAFU",               "dica": "Lateral direito brasileiro, capitão do tetracampeonato em 2002",           "cat": "🇧🇷 Lenda do Brasil"},
        {"palavra": "ROMARIO",            "dica": "Centroavante campeão em 1994, eleito melhor jogador da Copa",             "cat": "🇧🇷 Lenda do Brasil"},
    ]
}

MAX_ERROS = 6

# ══════════════════════════════════════════════
#  HELPERS DE DESENHO
# ══════════════════════════════════════════════

def draw_text(surf, text, font, color, x, y, anchor="topleft", alpha=255):
    surf2 = font.render(str(text), True, color)
    if alpha < 255:
        surf2.set_alpha(alpha)
    r = surf2.get_rect(**{anchor: (x, y)})
    surf.blit(surf2, r)
    return r

def draw_rect_r(surf, color, rect, radius=10, alpha=255, border=0, border_color=None):
    """Rect com cantos arredondados e alpha opcional."""
    if alpha < 255:
        s = pygame.Surface((rect[2], rect[3]), pygame.SRCALPHA)
        pygame.draw.rect(s, (*color, alpha), (0, 0, rect[2], rect[3]), border_radius=radius)
        surf.blit(s, (rect[0], rect[1]))
    else:
        pygame.draw.rect(surf, color, rect, border_radius=radius)
    if border and border_color:
        pygame.draw.rect(surf, border_color, rect, border, border_radius=radius)

def lerp_color(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))

# ══════════════════════════════════════════════
#  PARTÍCULAS
# ══════════════════════════════════════════════
class Particle:
    def __init__(self, x, y, color, vel=None):
        self.x = x + random.uniform(-20, 20)
        self.y = y + random.uniform(-10, 10)
        self.vx = vel[0] if vel else random.uniform(-3, 3)
        self.vy = vel[1] if vel else random.uniform(-8, -2)
        self.color = color
        self.life = 1.0
        self.decay = random.uniform(0.012, 0.025)
        self.r = random.randint(3, 8)

    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.vy += 0.15
        self.life -= self.decay
        return self.life > 0

    def draw(self, surf):
        alpha = int(self.life * 255)
        s = pygame.Surface((self.r*2, self.r*2), pygame.SRCALPHA)
        pygame.draw.circle(s, (*self.color, alpha), (self.r, self.r), self.r)
        surf.blit(s, (int(self.x - self.r), int(self.y - self.r)))

particles = []

def burst(x, y, color, n=30):
    for _ in range(n):
        particles.append(Particle(x, y, color))

# ══════════════════════════════════════════════
#  DESENHO DO CAMPO (background)
# ══════════════════════════════════════════════
def draw_field(surf):
    surf.fill(C["bg"])
    # listras do gramado
    stripe_h = 80
    for i in range(H // stripe_h + 1):
        col = C["field"] if i % 2 == 0 else C["field2"]
        pygame.draw.rect(surf, col, (0, i * stripe_h, W, stripe_h))
    # linhas do campo (decorativas)
    pygame.draw.rect(surf, C["line"], (30, 30, W-60, H-60), 2, border_radius=4)
    # círculo central
    pygame.draw.circle(surf, C["line"], (W//2, H//2), 120, 2)
    pygame.draw.line(surf, C["line"], (W//2, 30), (W//2, H-30), 2)
    # vinheta escura nas bordas
    vignette = pygame.Surface((W, H), pygame.SRCALPHA)
    for r in range(max(W, H), 0, -20):
        alpha = max(0, int(120 * (1 - r / max(W, H))))
        pygame.draw.circle(vignette, (0, 0, 0, alpha), (W//2, H//2), r)
    surf.blit(vignette, (0, 0))

# ══════════════════════════════════════════════
#  DESENHO DA FORCA  (SVG-like com pygame.draw)
# ══════════════════════════════════════════════
def draw_gallows(surf, erros, cx, cy, scale=1.0):
    W2 = int(10 * scale)
    GREEN  = C["green"]
    YELLOW = (220, 180, 40)
    RED    = C["red"]

    # cor dinâmica por estágio
    if erros < 2:
        mc = GREEN
    elif erros < 4:
        mc = YELLOW
    else:
        mc = RED

    # base
    bx, by = cx - int(70*scale), cy + int(140*scale)
    pygame.draw.rect(surf, mc, (bx, by, int(140*scale), W2), border_radius=4)
    # poste vertical
    pygame.draw.rect(surf, mc, (bx + int(20*scale), cy - int(120*scale), W2, int(260*scale)), border_radius=4)
    # braço horizontal
    pygame.draw.rect(surf, mc, (bx + int(20*scale), cy - int(120*scale), int(80*scale), W2), border_radius=4)
    # corda
    pygame.draw.rect(surf, mc, (bx + int(90*scale), cy - int(110*scale), int(5*scale), int(30*scale)))

    hx = bx + int(93*scale)
    hy = cy - int(80*scale)

    if erros >= 1:  # cabeça
        pygame.draw.circle(surf, mc, (hx, hy), int(20*scale), W2-2)
    if erros >= 2:  # corpo
        pygame.draw.line(surf, mc, (hx, hy + int(20*scale)), (hx, hy + int(70*scale)), W2)
    if erros >= 3:  # braço esq
        pygame.draw.line(surf, mc, (hx, hy + int(30*scale)), (hx - int(25*scale), hy + int(55*scale)), W2)
    if erros >= 4:  # braço dir
        pygame.draw.line(surf, mc, (hx, hy + int(30*scale)), (hx + int(25*scale), hy + int(55*scale)), W2)
    if erros >= 5:  # perna esq
        pygame.draw.line(surf, mc, (hx, hy + int(70*scale)), (hx - int(20*scale), hy + int(110*scale)), W2)
    if erros >= 6:  # perna dir
        pygame.draw.line(surf, mc, (hx, hy + int(70*scale)), (hx + int(20*scale), hy + int(110*scale)), W2)
        # olhos X
        pygame.draw.line(surf, RED, (hx-10, hy-10), (hx-4, hy-4), 3)
        pygame.draw.line(surf, RED, (hx-4, hy-10), (hx-10, hy-4), 3)
        pygame.draw.line(surf, RED, (hx+4, hy-10), (hx+10, hy-4), 3)
        pygame.draw.line(surf, RED, (hx+10, hy-10), (hx+4, hy-4), 3)

# ══════════════════════════════════════════════
#  BOTÃO  
# ══════════════════════════════════════════════
class Button:
    def __init__(self, rect, label, color=None, hover_color=None, font=None,
                 text_color=None, radius=10):
        self.rect = pygame.Rect(rect)
        self.label = label
        self.color = color or C["btn"]
        self.hover_color = hover_color or C["btn_hover"]
        self.font = font or F["btn"]
        self.text_color = text_color or C["white"]
        self.radius = radius
        self.hovered = False
        self._anim = 0.0

    def update(self, mouse):
        self.hovered = self.rect.collidepoint(mouse)
        target = 1.0 if self.hovered else 0.0
        self._anim += (target - self._anim) * 0.15

    def draw(self, surf):
        col = lerp_color(self.color, self.hover_color, self._anim)
        scale = 1.0 + 0.02 * self._anim
        r = self.rect.inflate(int(self.rect.w*(scale-1)), int(self.rect.h*(scale-1)))
        draw_rect_r(surf, col, r, self.radius)
        draw_rect_r(surf, C["gold"] if self.hovered else C["gold2"], r, self.radius,
                    border=2, border_color=C["gold"] if self.hovered else C["gold2"])
        draw_text(surf, self.label, self.font, self.text_color,
                  r.centerx, r.centery, anchor="center")

    def clicked(self, event):
        return (event.type == pygame.MOUSEBUTTONDOWN and
                event.button == 1 and self.rect.collidepoint(event.pos))

# ══════════════════════════════════════════════
#  TECLADO VIRTUAL (A–Z)
# ══════════════════════════════════════════════
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

class KeyboardUI:
    def __init__(self, cx, y_start):
        self.keys = {}
        self.states = {}  # "normal","correct","wrong"
        rows = ["QWERTYUIOP", "ASDFGHJKL", "ZXCVBNM"]
        kw, kh = 48, 46
        gap = 6
        for ri, row in enumerate(rows):
            offset = ri * (kw // 2 + gap // 2)
            row_w = len(row) * (kw + gap) - gap
            sx = cx - row_w // 2 + offset
            for ci, ch in enumerate(row):
                rx = sx + ci * (kw + gap)
                ry = y_start + ri * (kh + gap)
                self.keys[ch] = pygame.Rect(rx, ry, kw, kh)
                self.states[ch] = "normal"

    def reset(self):
        for ch in self.states:
            self.states[ch] = "normal"

    def mark(self, ch, state):
        if ch in self.states:
            self.states[ch] = state

    def draw(self, surf, mouse):
        for ch, rect in self.keys.items():
            state = self.states[ch]
            if state == "correct":
                bg = C["green"]
                tc = (10, 10, 10)
                bc = (60, 180, 70)
            elif state == "wrong":
                bg = (80, 20, 20)
                tc = (160, 60, 60)
                bc = (120, 30, 30)
            else:
                hov = rect.collidepoint(mouse)
                bg = C["btn_hover"] if hov else C["letter_bg"]
                tc = C["white"]
                bc = C["gold"] if hov else C["line"]
            draw_rect_r(surf, bg, rect, radius=6)
            draw_rect_r(surf, bc, rect, radius=6, border=2, border_color=bc)
            draw_text(surf, ch, F["letter"], tc, rect.centerx, rect.centery, anchor="center")

    def get_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for ch, rect in self.keys.items():
                if rect.collidepoint(event.pos) and self.states[ch] == "normal":
                    return ch
        return None

# ══════════════════════════════════════════════
#  ESTADO DO JOGO
# ══════════════════════════════════════════════
class GameState:
    MENU    = "menu"
    LEVEL   = "level"
    PLAYING = "playing"
    WIN     = "win"
    LOSE    = "lose"
    SCORE   = "score"

# ══════════════════════════════════════════════
#  TELA MENU
# ══════════════════════════════════════════════
class MenuScreen:
    def __init__(self):
        self.btn_play  = Button((W//2-120, 440, 240, 60), "▶  JOGAR",
                                 color=(30,90,50), hover_color=(50,140,70))
        self.btn_score = Button((W//2-120, 520, 240, 60), "🏅  PLACAR",
                                 color=(30,60,90), hover_color=(50,100,140))
        self.tick = 0
        self.ball_x = W // 2
        self.ball_y = 0
        self.ball_vy = 0
        self.ball_bouncing = True
        self._init_ball()

    def _init_ball(self):
        self.ball_x = random.randint(200, W-200)
        self.ball_y = -30
        self.ball_vy = random.uniform(4, 7)
        self.ball_vx = random.uniform(-2, 2)

    def update(self):
        self.tick += 1
        self.ball_x += self.ball_vx
        self.ball_y += self.ball_vy
        self.ball_vy += 0.25
        if self.ball_y > H + 40:
            self._init_ball()

    def draw(self, surf, mouse):
        draw_field(surf)
        # título
        t = self.tick * 0.03
        glow = int(200 + 55 * math.sin(t))
        draw_text(surf, "FORCA DA", F["title"],
                  (glow, 220, 80), W//2, 130, anchor="center")
        draw_text(surf, "COPA DO MUNDO 2026", F["sub"],
                  C["gold"], W//2, 215, anchor="center")
        draw_text(surf, "⚽  Adivinhe palavras sobre a história das Copas  ⚽",
                  F["small"], C["gray"], W//2, 270, anchor="center")
        # países-sede
        draw_text(surf, "🇺🇸 EUA  •  🇨🇦 Canadá  •  🇲🇽 México",
                  F["body"], C["gray"], W//2, 310, anchor="center")
        # mini forca decorativa
        draw_gallows(surf, 3, W//2, 390, scale=0.7)
        # bola
        pygame.draw.circle(surf, C["white"], (int(self.ball_x), int(self.ball_y)), 14)
        pygame.draw.circle(surf, C["field"], (int(self.ball_x), int(self.ball_y)), 14, 2)
        # botões
        self.btn_play.update(mouse)
        self.btn_score.update(mouse)
        self.btn_play.draw(surf)
        self.btn_score.draw(surf)
        draw_text(surf, "Pressione qualquer letra para começar | ESC para sair",
                  F["tiny"], C["gray"], W//2, H-22, anchor="center")

    def handle(self, event):
        if self.btn_play.clicked(event):
            return GameState.LEVEL
        if self.btn_score.clicked(event):
            return GameState.SCORE
        if event.type == pygame.KEYDOWN and event.key not in (pygame.K_ESCAPE, pygame.K_RETURN):
            return GameState.LEVEL
        return None

# ══════════════════════════════════════════════
#  TELA ESCOLHA DE NÍVEL
# ══════════════════════════════════════════════
LEVELS = [
    ("facil",   "🟢  FÁCIL",   "Jogadores famosos, países, básicos",            (30,130,60)),
    ("medio",   "🟡  MÉDIO",   "Lendas, Copa 2026, estatísticas",               (140,120,20)),
    ("dificil", "🔴  DIFÍCIL", "Recordes históricos, estádios, jovens talentos",(130,30,30)),
]

class LevelScreen:
    def __init__(self):
        self.btns = []
        for i, (key, label, desc, col) in enumerate(LEVELS):
            y = 260 + i * 120
            self.btns.append({
                "key": key, "label": label, "desc": desc,
                "btn": Button((W//2-220, y, 440, 80), label,
                               color=col,
                               hover_color=tuple(min(255, c+40) for c in col),
                               radius=14)
            })
        self.back = Button((30, H-70, 120, 44), "← Voltar",
                            color=(40,40,40), hover_color=(70,70,70))

    def draw(self, surf, mouse):
        draw_field(surf)
        draw_text(surf, "Escolha o nível de dificuldade", F["sub"],
                  C["gold"], W//2, 160, anchor="center")
        draw_text(surf, "Mais difícil = mais pontos",
                  F["small"], C["gray"], W//2, 205, anchor="center")
        for item in self.btns:
            item["btn"].update(mouse)
            item["btn"].draw(surf)
            # descrição embaixo do botão
            r = item["btn"].rect
            draw_text(surf, item["desc"], F["small"], C["gray"],
                      W//2, r.bottom + 8, anchor="center")
        self.back.update(mouse)
        self.back.draw(surf)

    def handle(self, event):
        for item in self.btns:
            if item["btn"].clicked(event):
                return item["key"]
        if self.back.clicked(event):
            return "back"
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            return "back"
        return None

# ══════════════════════════════════════════════
#  TELA DE JOGO
# ══════════════════════════════════════════════
class PlayScreen:
    def __init__(self, nivel, pool, pontos_acumulados, historico):
        self.nivel = nivel
        self.pool  = pool
        self.pontos= pontos_acumulados
        self.historico = historico
        self.pergunta = self.pool.pop()
        self.palavra  = self.pergunta["palavra"].upper()
        self.dica     = self.pergunta["dica"]
        self.cat      = self.pergunta["cat"]
        self.certas   = set()
        self.erradas  = set()
        self.erros    = 0
        self.dica_usada = False
        self.tick = 0
        self.msg  = ""
        self.msg_timer = 0
        self.result = None  # "win" | "lose"
        self.result_timer = 0

        self.kb = KeyboardUI(W//2, H - 185)
        base_pts = {"facil": 100, "medio": 200, "dificil": 350}
        self.base_pts = base_pts.get(nivel, 100)

        # botão dica
        self.btn_dica = Button((W - 210, 30, 180, 42), "💡 Dica (-40%)",
                                color=(60,50,10), hover_color=(100,80,15),
                                font=F["small"])
        # botão desistir
        self.btn_desist = Button((W - 210, 82, 180, 42), "🏳 Desistir",
                                  color=(70,15,15), hover_color=(110,25,25),
                                  font=F["small"])

    def _check_win(self):
        palavra_letras = set(c for c in self.palavra if c != " ")
        return palavra_letras.issubset(self.certas)

    def _guess(self, letra):
        if letra in self.certas or letra in self.erradas:
            return
        if letra in self.palavra:
            self.certas.add(letra)
            self.kb.mark(letra, "correct")
            burst(W//2, H//2 - 50, C["green"], 20)
            if self._check_win():
                pts = self.base_pts if not self.dica_usada else int(self.base_pts * 0.6)
                self.pontos += pts
                self.historico.append((self.palavra, True, pts))
                self.result = "win"
                self.result_timer = 0
                burst(W//2, H//2, C["gold"], 60)
        else:
            self.erradas.add(letra)
            self.kb.mark(letra, "wrong")
            self.erros += 1
            if self.erros >= MAX_ERROS:
                self.historico.append((self.palavra, False, 0))
                self.result = "lose"
                self.result_timer = 0

    def update(self):
        self.tick += 1
        if self.msg_timer > 0:
            self.msg_timer -= 1
        if self.result:
            self.result_timer += 1

        # atualiza partículas
        particles[:] = [p for p in particles if p.update()]

    def draw(self, surf, mouse):
        draw_field(surf)

        # ── painel esquerdo (forca + info)
        draw_rect_r(surf, C["panel"], (20, 20, 310, H-40), radius=14, alpha=200)

        nivel_label = {"facil":"🟢 FÁCIL","medio":"🟡 MÉDIO","dificil":"🔴 DIFÍCIL"}.get(self.nivel,"")
        draw_text(surf, nivel_label, F["cat"], C["gold"], 175, 38, anchor="center")
        draw_text(surf, self.cat, F["cat"], C["gray"], 175, 62, anchor="center")

        draw_gallows(surf, self.erros, 175, 260, scale=1.15)

        # erros / max
        err_col = C["green"] if self.erros < 3 else C["gold"] if self.erros < 5 else C["red"]
        draw_text(surf, f"Erros: {self.erros}/{MAX_ERROS}", F["body"],
                  err_col, 175, H//2 + 50, anchor="center")

        # letras erradas
        draw_text(surf, "Letras erradas:", F["small"], C["gray"], 175, H//2 + 90, anchor="center")
        erradas_str = "  ".join(sorted(self.erradas)) if self.erradas else "—"
        draw_text(surf, erradas_str, F["body"], C["red"], 175, H//2 + 115, anchor="center")

        # pontuação
        draw_text(surf, f"Pontos: {self.pontos}", F["small"], C["gold"], 175, H-70, anchor="center")
        draw_text(surf, f"Rodadas: {len(self.historico)}", F["small"], C["gray"], 175, H-48, anchor="center")

        # ── área principal
        # dica
        if self.dica_usada:
            draw_rect_r(surf, (20,40,10), (340, 28, W-360, 56), radius=10, alpha=180)
            draw_text(surf, f"💡  {self.dica}", F["hint"], C["gold"], W//2, 56, anchor="center")
        else:
            self.btn_dica.update(mouse)
            self.btn_dica.draw(surf)

        self.btn_desist.update(mouse)
        self.btn_desist.draw(surf)

        # palavra
        word_y = 170
        draw_text(surf, "ADIVINHE A PALAVRA:", F["small"], C["gray"], W//2, word_y - 35, anchor="center")
        
        # monta display
        chars = []
        for ch in self.palavra:
            if ch == " ":
                chars.append(("  ", False))
            elif ch in self.certas:
                chars.append((ch, True))
            else:
                chars.append(("_", False))

        total_w = 0
        spacing = 10
        char_surfs = []
        for ch, revealed in chars:
            col = C["green"] if revealed else C["white"]
            s = F["word"].render(ch, True, col)
            char_surfs.append((s, revealed, ch))
            total_w += s.get_width() + spacing

        sx = W//2 - total_w//2 + 155
        for s, revealed, ch in char_surfs:
            screen.blit(s, (sx, word_y))
            # underline
            uw = s.get_width()
            py = word_y + s.get_height() + 3
            pygame.draw.line(surf, C["green"] if revealed else C["gray"],
                             (sx, py), (sx + uw, py), 2)
            sx += s.get_width() + spacing

        # teclado
        self.kb.draw(surf, mouse)
        draw_text(surf, "Clique nas letras ou pressione o teclado",
                  F["tiny"], C["gray"], W//2, H - 195, anchor="center")

        # partículas
        for p in particles:
            p.draw(surf)

        # overlay resultado
        if self.result:
            self._draw_result(surf)

    def _draw_result(self, surf):
        alpha = min(220, int(self.result_timer * 5))
        ov = pygame.Surface((W, H), pygame.SRCALPHA)
        bg = (10, 60, 30, alpha) if self.result == "win" else (60, 10, 15, alpha)
        ov.fill(bg)
        surf.blit(ov, (0, 0))

        if self.result == "win":
            msg1 = "🏆  ACERTOU!"
            msg2 = f"A palavra era: {self.palavra}"
            col1 = C["gold"]
        else:
            msg1 = "☠️  GAME OVER"
            msg2 = f"A palavra era: {self.palavra}"
            col1 = C["red"]

        a = min(255, self.result_timer * 8)
        draw_text(surf, msg1, F["stage_title"], col1, W//2, H//2 - 60, anchor="center", alpha=a)
        draw_text(surf, msg2, F["sub"], C["white"], W//2, H//2 + 10, anchor="center", alpha=a)
        if self.result_timer > 50:
            draw_text(surf, "Clique em qualquer lugar para continuar",
                      F["small"], C["gray"], W//2, H//2 + 70, anchor="center")

    def handle(self, event):
        # overlay ativo — qualquer clique continua
        if self.result and self.result_timer > 50:
            if event.type in (pygame.MOUSEBUTTONDOWN, pygame.KEYDOWN):
                return self.result  # "win" ou "lose"
            return None

        # dica
        if self.btn_dica.clicked(event) and not self.dica_usada:
            self.dica_usada = True
            return None

        # desistir
        if self.btn_desist.clicked(event):
            self.historico.append((self.palavra, False, 0))
            self.result = "lose"
            self.result_timer = 0
            return None

        # teclado virtual
        letra = self.kb.get_clicked(event)
        if letra:
            self._guess(letra)
            return None

        # teclado físico
        if event.type == pygame.KEYDOWN:
            key_name = pygame.key.name(event.key).upper()
            if len(key_name) == 1 and key_name.isalpha():
                self._guess(key_name)

        return None

# ══════════════════════════════════════════════
#  TELA PÓS-RODADA (próxima / mudar nível / placar)
# ══════════════════════════════════════════════
class PostRoundScreen:
    def __init__(self, resultado, palavra, pontos, historico, nivel):
        self.resultado = resultado
        self.palavra   = palavra
        self.pontos    = pontos
        self.historico = historico
        self.nivel     = nivel
        cy = H//2 + 20
        self.btn_next  = Button((W//2-220, cy+20,  200, 56), "▶  Próxima",
                                 color=(30,100,50))
        self.btn_level = Button((W//2+20,  cy+20,  200, 56), "⚙  Mudar Nível",
                                 color=(50,50,10), hover_color=(90,90,20))
        self.btn_score = Button((W//2-110, cy+95,  220, 50), "🏅  Ver Placar",
                                 color=(20,40,80), hover_color=(40,70,130))
        self.tick = 0

    def update(self):
        self.tick += 1
        particles[:] = [p for p in particles if p.update()]

    def draw(self, surf, mouse):
        draw_field(surf)
        col1 = C["gold"] if self.resultado == "win" else C["red"]
        msg  = "🏆  ACERTOU!" if self.resultado == "win" else "☠️  ERROU..."
        draw_text(surf, msg, F["stage_title"], col1, W//2, H//2 - 120, anchor="center")
        draw_text(surf, f"A palavra era:  {self.palavra}", F["sub"],
                  C["white"], W//2, H//2 - 50, anchor="center")
        draw_text(surf, f"Pontuação total: {self.pontos} pts", F["score"],
                  C["gold"], W//2, H//2 + 5, anchor="center")

        for p in particles:
            p.draw(surf)

        for btn in (self.btn_next, self.btn_level, self.btn_score):
            btn.update(mouse)
            btn.draw(surf)

    def handle(self, event):
        if self.btn_next.clicked(event):
            return "next"
        if self.btn_level.clicked(event):
            return "level"
        if self.btn_score.clicked(event):
            return "score"
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                return "next"
            if event.key == pygame.K_ESCAPE:
                return "level"
        return None

# ══════════════════════════════════════════════
#  TELA DE PLACAR
# ══════════════════════════════════════════════
class ScoreScreen:
    def __init__(self, historico, pontos):
        self.historico = historico
        self.pontos    = pontos
        self.btn_menu  = Button((W//2-110, H-80, 220, 50), "🏠  Menu Inicial",
                                 color=(30,60,30), hover_color=(50,100,50))
        self.scroll = 0

    def draw(self, surf, mouse):
        draw_field(surf)
        draw_rect_r(surf, C["panel"], (W//2-300, 20, 600, H-40), radius=16, alpha=210)
        draw_text(surf, "🏅  PLACAR DA SESSÃO", F["sub"], C["gold"],
                  W//2, 50, anchor="center")

        acertos = sum(1 for _, ok, _ in self.historico if ok)
        total   = sum(p for _, _, p in self.historico)
        draw_text(surf, f"Rodadas: {len(self.historico)}   Acertos: {acertos}   Total: {total} pts",
                  F["small"], C["white"], W//2, 90, anchor="center")

        pygame.draw.line(surf, C["line"], (W//2-260, 115), (W//2+260, 115), 1)

        # lista (com scroll simples)
        y = 130 + self.scroll
        for i, (palavra, ok, pts) in enumerate(self.historico):
            if y > H - 100:
                break
            if y > 115:
                icon = "✔" if ok else "✘"
                ic   = C["green"] if ok else C["red"]
                draw_text(surf, f"{i+1:2}.", F["small"], C["gray"], W//2-230, y)
                draw_text(surf, icon, F["body"], ic, W//2-190, y)
                draw_text(surf, palavra, F["body"], C["white"], W//2-155, y)
                draw_text(surf, f"+{pts} pts", F["small"], C["gold"], W//2+180, y, anchor="topright")
            y += 32

        # classificação
        pygame.draw.line(surf, C["line"], (W//2-260, H-150), (W//2+260, H-150), 1)
        if total >= 1000:
            rank = "🥇  FENÔMENO DA COPA!"
        elif total >= 500:
            rank = "🥈  CRAQUE DO FUTEBOL!"
        elif total >= 200:
            rank = "🥉  TORCEDOR DEDICADO"
        else:
            rank = "⚽  CONTINUE ESTUDANDO!"
        draw_text(surf, rank, F["body"], C["gold"], W//2, H-130, anchor="center")

        self.btn_menu.update(mouse)
        self.btn_menu.draw(surf)

    def handle(self, event):
        if self.btn_menu.clicked(event):
            return "menu"
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return "menu"
            if event.key == pygame.K_DOWN:
                self.scroll -= 32
            if event.key == pygame.K_UP:
                self.scroll = min(0, self.scroll + 32)
        if event.type == pygame.MOUSEWHEEL:
            self.scroll += event.y * 20
            self.scroll = min(0, self.scroll)
        return None

# ══════════════════════════════════════════════
#  LOOP PRINCIPAL
# ══════════════════════════════════════════════
def main():
    state     = GameState.MENU
    nivel     = "facil"
    pool      = []
    pontos    = 0
    historico = []

    screen_obj = MenuScreen()
    level_sel  = None

    running = True
    while running:
        mouse = pygame.mouse.get_pos()
        events = pygame.event.get()

        for event in events:
            if event.type == pygame.QUIT:
                running = False

            if state == GameState.MENU:
                r = screen_obj.handle(event)
                if r == GameState.LEVEL:
                    state = GameState.LEVEL
                    screen_obj = LevelScreen()
                elif r == GameState.SCORE:
                    state = GameState.SCORE
                    screen_obj = ScoreScreen(historico, pontos)

            elif state == GameState.LEVEL:
                r = screen_obj.handle(event)
                if r and r != "back":
                    nivel = r
                    pool  = PERGUNTAS[nivel].copy()
                    random.shuffle(pool)
                    state = GameState.PLAYING
                    screen_obj = PlayScreen(nivel, pool, pontos, historico)
                elif r == "back":
                    state = GameState.MENU
                    screen_obj = MenuScreen()

            elif state == GameState.PLAYING:
                r = screen_obj.handle(event)
                if r in ("win", "lose"):
                    pontos    = screen_obj.pontos
                    historico = screen_obj.historico
                    pool      = screen_obj.pool
                    state = GameState.WIN if r == "win" else GameState.LOSE
                    screen_obj = PostRoundScreen(r, screen_obj.palavra,
                                                  pontos, historico, nivel)
                    if r == "win":
                        burst(W//2, H//2, C["gold"], 80)

            elif state in (GameState.WIN, GameState.LOSE):
                r = screen_obj.handle(event)
                if r == "next":
                    if not pool:
                        pool = PERGUNTAS[nivel].copy()
                        random.shuffle(pool)
                    state = GameState.PLAYING
                    screen_obj = PlayScreen(nivel, pool, pontos, historico)
                elif r == "level":
                    state = GameState.LEVEL
                    screen_obj = LevelScreen()
                elif r == "score":
                    state = GameState.SCORE
                    screen_obj = ScoreScreen(historico, pontos)

            elif state == GameState.SCORE:
                r = screen_obj.handle(event)
                if r == "menu":
                    state = GameState.MENU
                    screen_obj = MenuScreen()

            # ESC global
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                if state not in (GameState.MENU,):
                    state = GameState.MENU
                    screen_obj = MenuScreen()

        # Update
        if hasattr(screen_obj, "update"):
            screen_obj.update()

        # Draw
        screen_obj.draw(screen, mouse)
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
