function [] = ej9() #M cantidad de partículas a generar
  M=30; #cantidad de pasos de cada partícula
  N=100; #cantidad de partículas
  A=zeros([M 2*N]);
  for z=1:2:(2*N) #z numero de columna, este for asigna el valor inicial de cada partícula y los siguientes 
    A(1,z)=randi([0, 100]); #elige al azar la posición incial 
    A(1,z+1)=randi([0, 200]);
    r=rand(M,1);
    
    for i=2:M #simula todos los movimientos de una partícula
      if r(i)>=0 && r(i)<=0.25
        A(i,z+1)=A(i-1,z+1)+1; #que se mueva hacia arriba
        A(i,z)=A(i-1,z);
      elseif r(i)>0.25 && r(i)<=0.5
        A(i,z)=A(i-1,z)+1; #que se mueva hacia abajo
        A(i,z+1)=A(i-1,z+1);
      elseif r(i)>0.5 && r(i)<=0.75
        A(i,z+1)=A(i-1,z+1)-1; #que se mueva hacia la izquierda
        A(i,z)=A(i-1,z);
      else
        A(i,z)=A(i-1,z)-1; #que se mueva hacia la derecha
        A(i,z+1)=A(i-1,z+1);
      end
    end
  end
  
  figure(1)
  for a=1:M
    for b=1:2:(2*N)
      axis([0, 100, 0, 200]);
      plot(A(a,b), A(a, b+1), "b*");
      hold on;
    end 
    hold off;
    drawnow;  
  end
  
end