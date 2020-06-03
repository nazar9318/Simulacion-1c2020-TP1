function [] = ej8()
  N=1000;
  x=zeros(N,1); #vector de posición en x, inicializado en 0
  y=zeros(N,1); #vector de posición en x, inicializado en 0
  r=rand(N,1);
  
  for i=2:N #bucle que establece los movientos de toda una partícula de acuerdo al vector random
    if r(i)>=0 && r(i)<=0.25
      y(i)=y(i-1)+1;  #que se mueva hacia arriba
      x(i)=x(i-1);
    elseif r(i)>0.25 && r(i)<=0.5
      x(i)=x(i-1)+1; #que se mueva hacia abajo
      y(i)=y(i-1);
    elseif r(i)>0.5 && r(i)<=0.75
      y(i)=y(i-1)-1;  #que se mueva hacia la izquierda
      x(i)=x(i-1);
    else
      x(i)=x(i-1)-1;  #que se mueva hacia la derecha
      y(i)=y(i-1);
    end
  end
  #set (0, "defaultaxesfontname", "Helvetica"); #lo que sigue es el gráfico final del RW con la configuración para guardarlo como imagen 
  #figure(1)
  #plot(x,y, "r");
  #title('Random walking simple');
  #xlabel ('Posición en x');
  #ylabel ('Posisicón en y');
  #print -djpg ej8.jpg;
  figure(2)
  title('Random walking simple');  
  xlabel ('Posición en x');
  ylabel ('Posisicón en y');
  hold on;
  comet(x,y); #dibuja el recorrido de la partícula dejando trazado el camino recorrido


end