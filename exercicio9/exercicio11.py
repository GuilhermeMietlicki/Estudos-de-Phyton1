larg = float(input('largura da parede'))
alt = float(input('Altura da parede'))
area = larg * alt
print('Sua parede te, a dimensão de {}x{} e sua area é de {}m.'.format(larg, alt, area))
tinta = area / 2
print('Para pintar essa parede, você precisará de {}L de tinta'.format(tinta))
