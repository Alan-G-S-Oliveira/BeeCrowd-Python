N1, N2, N3, N4 = input().split()

N1 = float(N1)
N2 = float(N2)
N3 = float(N3)
N4 = float(N4)

media = (N1 * 2 + N2 * 3 + N3 * 4 + N4 * 1) / 10

print("Media: %.1f"% media)

if media >= 7:
    print("Aluno aprovado.")
elif media < 5:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    
    nota_exame = float(input())
    print("Nota do exame: %.1f"% nota_exame)
    
    media_final = (media + nota_exame) / 2
    
    if media_final >= 5:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    
    print("Media final: %.1f"% media_final)