#A través del método de aceptación/rechazo genera números aleatorios con distribución Normal(25,2)
#y lo compara con el generador de Octave
function [] = ej4() 
  N=100000;
  c = exp((-(4^2)/8+4))/(2*sqrt(2*pi));
  #disp(c);
  t = exprnd(1,1,N); #Genera un vector de 1xN muestras de exponenciales de lambda=1
  p = fX(t)./(c*fY(t)); #Genera un vector de probabilidades de aceptar
  z = [];

for i=1:N
    r = rand(1);
    if r < p(i) #acepta t(i) con probabilidad p(i)
        r2 = rand();
        if r2 < 0.5 #con probabilidad 0.5 lo deja positivo
            z = [z, t(i)];
        else  #con probabilidad 0.5 lo hace negativo
            z = [z, -t(i)];
        end
    end 
end

  z2=z+25; #corre todos los valores aceptados de manera que quede centrado en 25

  #disp(['Porcentaje de rechazo = ', num2str((N-length(z))/N)])

  disp(['La media de la distribución simulada es = ', num2str(mean(z2))])
  disp(['El desvío estándar de la distribución simulada es = ', num2str(sqrt(var(z)))])

  set (0, "defaultaxesfontname", "Helvetica");
  figure;
  hist(z2, 16,1, "b");
  hold;
  title('Histograma de los números generados por el método de aceptación/rechazo');
  #figure();
  #normplot(z2);
  r = normrnd(25,2,[1,length(z)]); #vector de N filas y 1 columna de números aleatorios con distribución N(25, 2)
  plot(r, normpdf(r,25,2), "r.");
  title('Normal(25,2)');
  print -djpg ej4.jpg;
  
end


function f = fY(y) #Función que sé generar
 f=exp(-y);
end


function f = fX(x) #Función de distribución que quiero generar
 f = exp((-x.^2)/8)/(sqrt(2*pi)*2);
end