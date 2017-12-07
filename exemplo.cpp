
   ini = 0
   while(ini < len(lista)):

       atual = lista[ini]
       ini+=1

       for i in range(len(G[atua])):

           v = grafo[atual][i]

           grau[v] -= 1
           if(grau[v] == 0):
                lista.append(v) // se o grau se tornar zero, acrescenta-se a lista
                print v


   // agora, se na lista não houver N vértices,
   // sabemos que é impossível realizar o procedimento

   if((int)lista.size() < n) printf("impossivel\n");
   else{
       for(int i = 0;i < (int)lista.size();i++) printf("%d ", lista[i]);
       printf("\n");
   }
