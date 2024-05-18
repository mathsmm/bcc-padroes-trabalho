### Strategy

Usar para adaptar corpos novos adicionados no simulador. Se eu quiser adicionar um retângulo que se move, vou precisar criar uma classe nova. Se eu precisar colocar um círculo que atrai outros círculos, também vou precisar criar uma classe nova. Utilizamos então o Strategy com comportamentos como: `can_move`, `can_attract`, `can_collide`, etc, na classe Body.