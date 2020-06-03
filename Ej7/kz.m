function ks()
    z2= normalRandom(100000);
    disp(['La media de la distribución simulada es = ', num2str(mean(z2))])
    disp(['El desvío estándar de la distribución simulada es = ', num2str(sqrt(var(z2)))])
    
    #KS test
    
    X=sort(z2);
    #Determinamos la distribucion acumulativa empirica:
    dist_emp=empirical_cdf(X,X);
    #Determinamos la distribucion esperada acumulativa:
    n = normrnd(25,2,[length(z2),1]); #vector de N filas y 1 columna de números aleatorios con distribución N(25, 2)
    n=sort(n);
    dist_esp_acum=normcdf(n,25,2) #sera la hipotesis nula
    
    #El estadístico k es el maximo de la diferencia entre las dos distribuciones acumulativas:
    k=max(abs(dist_esp_acum-dist_emp));

    #grafico la empirica y la distribucion esperada acumulativa 
    figure;
   
    plot(n,dist_esp_acum,'b');
    hold on;
    plot(X,dist_emp,'m');
    h = legend ({"Dist. Esperada Acum.", "Dist. Empirica Acum."});
    legend ("left");
    legend (h,"location", "northwest");
    set (h, "fontsize", 16);
    set (h, "textposition", "left");
    legend boxoff
    p = kolmogorov_smirnov_test_2(dist_emp,dist_esp_acum);
    disp(['pvalor: ', num2str(p)]);
  
end

function z2 = normalRandom(N)

    c = exp((-(4^2)/8+4))/(2*sqrt(2*pi));
    t = exprnd(1,1,N); #Genera un vector de 1xN muestras de exponenciales de lambda=1
    p = (exp((-t.^2)/8)/(sqrt(2*pi)*2))./(c*(exp(-t))); #Genera un vector de probabilidades de aceptar
    z = [];

    for i=1:N
        r = rand(1);
        if r < p(i) #acepto t(i) con prob. p(i)
            r2 = rand();
            if r2 < 0.5 #con prob 0.5 lo deja positivo
                z = [z, t(i)];
            else  #con prob 0.5 lo hace negativo
                z = [z, -t(i)];
            end
        end 
    end

    z2=z+25; #corre todos los valores aceptados de manera que quede centrado en 25
end