% 111c51502
% CY Fu
% NTUT-UTA AI-EMBA Program
% 2023/09/23

m=[2 5 10 20 50 100 200 500 1000]; 
n_limit=[100 100 100 100 150 300 400 500 500]; 
pc1=0.5; 
pc2=0.5; 
for t=1:9 
    p=[]; 
    g=0; 
    m1=floor(pc1*m(t)); 
    m2=floor(pc2*m(t)); 
    for n=1:1000 
        if n>n_limit(t) 
            break; 
        end 
        pcr=0; 
        if n==1 
            pcr=0.5; 
        else 
            for r=0:m2 
                for s=0:m1 
                    if s>r 
                        g=n*((n-1)^2)*pc1*(s+1)/(m1+n); 
                    else 
                        g=n*((n-1)^2)*pc2*(r+1)/(m2+n); 
                    end 
                    % pcr=pcr+(g*prod(m2-r+1:m2-r+n-2)/prod(m2+1:m2+n-1)*prod(m1-s+1:m1-s+n-2)/prod(m1+1:m1+n-1));
                    log_pcr_term = log(g) + sum(log(m2-r+1:m2-r+n-2)) - sum(log(m2+1:m2+n-1)) + sum(log(m1-s+1:m1-s+n-2)) - sum(log(m1+1:m1+n-1));
                    pcr = pcr + exp(log_pcr_term);
                end 
            end 
        end

        p=[p [pcr;n]]; 
    end 
 semilogx(p(2,:),p(1,:)) 
 if m(t)==2 
     nStr=['m= ' num2str(m(t))]; 
     text(p(2,size(p,2)),p(1,size(p,2))-0.005,nStr) 
 else 
     nStr=[num2str(m(t))]; 
     text(p(2,size(p,2))+2,p(1,size(p,2)),nStr) 
 end 
 hold on 
end 
xlim([1 1000])
ylim([0.49 0.76])
grid()
title({'pr_hw#01_111c51502' ; 'Finite Data Set Accuracy (Pc1=1/2)'}, 'Interpreter', 'none')
set(gca,'XTick',[1,2,3,4,5,10,20,50,100,200,500,1000])
set(gca,'XTickLabel',{'1','2','3','4','5','10','20','50','100','200','500','1000'})
xlabel('MEASUREMENT COMPLEXITY n (TOTAL DISCRETE VALUES)')
ylabel('MEAN RECOGNITION ACCURACY Pcr(n,m,Pc1)')

