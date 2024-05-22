from src.vec2 import Vec2
from src.circle_body import CircleBody
from src.rect_body import RectBody

def clamp(value: float, min_v: float, max_v: float):
    return max(min_v, min(value, max_v))

class CollisionLogic:
    def circle_circle_collision(c1: CircleBody, c2: CircleBody):
        # Se o produto escalar entre o vetor formado pelos vetores de posição
        # e o vetor formado pelos vetores de velocidade for maior ou igual
        # a zero, os corpos circulares não estão se aproximando
        if Vec2(c1.pos, c2.pos) * Vec2(c1.vel, c2.vel) >= 0:
            return None
        
        # Se a soma dos raios dos corpos circulares for menor que a distância 
        # entre as posições deles, não há colisão
        if (c1.radius + c2.radius) < Vec2.s_distance_between(c1.pos, c2.pos):
            return None
        
        # Para maiores esclarecimentos,
        # https:#www.vobarian.com/collisions/2dcollisions2.pdf

        # Acrônimos:
        # v  -> Vetor
        # uV -> Vetor unitário
        # 1  -> Referente ao corpo circular 1
        # 2  -> Referente ao corpo circular 2
        # N  -> Normal (perpendicular)
        # T  -> Tangente
        # B  -> Before collision (Antes da colisão)
        # A  -> After collision (Depois da colisão)
        # c  -> Componente (grandeza escalar)
        # m  -> Massa

        # Passo 1 - Achar vetor unitário normal e vetor unitário tangente.
        # Eles formam "eixos" que serão utilizados em passos seguintes

        # "Eixo y"
        uVN: Vec2 = Vec2(c1.pos, c2.pos).unit()
        
        # "Eixo x"
        uVT: Vec2 = Vec2(-uVN.y, uVN.x)

        # Passo 2 - Criar os vetores de velocidade inicial 
        # (antes da colisão) de ambos os corpos circulares. 
        # OBS: Eles já existem (obj_corpo_circular.velocidade)

        # Passo 3 - Projetar os vetores de velocidade inicial
        # nos vetores unitários normal e tangente.
        # Isto pode ser feito ao efetuar o produto escalar entre
        # os vetores unitários e os vetores de velocidade
        v1NBc: Vec2 = uVN * c1.vel
        v1TBc: Vec2 = uVT * c1.vel
        v2NBc: Vec2 = uVN * c2.vel
        v2TBc: Vec2 = uVT * c2.vel

        # Passo 4 - Encontrar as velocidades tangenciais
        # pós-colisão. Elas são iguais às pré-colisão
        v1TAc: Vec2 = v1TBc
        v2TAc: Vec2 = v2TBc

        # Passo 5 - Encontrar as velocidades normais
        # pós-colisão. Utiliza-se as fórmulas de momento
        # e de energia cinética em uma dimensão
        m1: float = c1.mass
        m2: float = c2.mass
        v1NAc: Vec2 = (v1NBc * (m1 - m2) + 2 * m2 * v2NBc) / (m1 + m2)
        v2NAc: Vec2 = (v2NBc * (m2 - m1) + 2 * m1 * v1NBc) / (m1 + m2)

        # Passo 6 - Converter componentes normais e 
        # tangenciais em vetores
        v1NA: Vec2 = uVN * v1NAc
        v1TA: Vec2 = uVT * v1TAc
        v2NA: Vec2 = uVN * v2NAc
        v2TA: Vec2 = uVT * v2TAc

        # Passo 7 - Encontrar os vetores de velocidade
        # pós-colisão e aplicá-los aos corpos circulares
        c1.vel = v1NA + v1TA
        c2.vel = v2NA + v2TA

    def circle_rect_collision(c: CircleBody, r: RectBody):
        pass