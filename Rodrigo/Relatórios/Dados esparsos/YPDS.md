Lendo os dados
--------------

``` r
setwd('/home/rodrigo/Dropbox/UNICAMP/MC886/trabalho/ProjetoY')
full_data = read.csv("YPDS.csv", header=T)

x_data = full_data[,-1]
y_data = factor(full_data[,1])
```

Dimensoes e características dos dados
-------------------------------------

``` r
dim(full_data)
```

    ## [1] 95 54

Balanceamento das classes.

``` r
summary(y_data)
```

    ##  0  1  2  3  4 
    ## 19 29  8 20 19

Podemos perceber que os dados estão levemente balanceados, distoando apenas na classe 1(29%) e 2(8%).

Verificando os dados faltantes.

``` r
sum(is.na(x_data))/(dim(x_data)[1]*dim(x_data)[2])
```

    ## [1] 0.1443893

Os dados faltantes representam quase 15% dos nossos dados.

O problema dos dados faltantes
------------------------------

Podemos ver a porcentagem de dados faltantes nas features(colunas) e nas observacoes(linhas).

Podemos ver a porcentagem de dados faltantes em cada feature.

``` r
apply(x_data,2,pMiss)
```

    ##        X37cgrowth        X40cgrowth X50.glucosegrowth X60.glucosegrowth 
    ##         11.578947         52.631579         25.263158         24.210526 
    ##    acidproduction      acidtolerant      amdglucoside arbutinhydrolysis 
    ##         12.631579         53.684211         13.684211          2.105263 
    ##        cadaverine        cellobiose        citricacid   cyclohex1000ppm 
    ##         45.263158          1.052632         24.210526         35.789474 
    ##    cyclohex100ppm        darabinose        erythritol           ethanol 
    ##         11.578947          4.210526          4.210526         12.631579 
    ##        ethylamine        galactitol         galactose    gluconolactone 
    ##          6.315789         14.736842          0.000000         27.368421 
    ##       glucosamine           glucose          glycerol          inositol 
    ##         28.421053          0.000000          6.315789          8.421053 
    ##            inulin              kno3        lacticacid           lactose 
    ##          5.263158          2.105263         11.578947          1.052632 
    ##        larabinose         lipolytic            lysine           maltose 
    ##          6.315789          8.421053         63.157895          1.052632 
    ##          mannitol         melibiose        melizitose          methanol 
    ##          3.157895          4.210526          4.210526         28.421053 
    ##           nh42so4         raffinose          rhamnose           ribitol 
    ##          5.263158          6.315789          8.421053          7.368421 
    ##            ribose           salicin     solublestarch          sorbitol 
    ##          6.315789          1.052632          8.421053          4.210526 
    ##           sorbose  starchproduction      succinicacid           sucrose 
    ##          6.315789          9.473684         11.578947          1.052632 
    ##         trehalose    ureaseactivity vitaminfreegrowth           xylitol 
    ##          4.210526         25.263158         44.210526         46.315789 
    ##            xylose 
    ##          4.210526

Como podemos ver, 34 colunas com mais de 5% de NA. 22 colunas com mais de 10%. 14 colunas com mais de 15% de NA.

Podemos ver a porcentagem de dados faltantes em cada obeservacao.

``` r
apply(x_data,1,pMiss)
```

    ##  [1]  1.886792  5.660377  3.773585  3.773585 20.754717  3.773585  5.660377
    ##  [8] 15.094340 41.509434  1.886792  3.773585  3.773585 75.471698  1.886792
    ## [15] 58.490566  9.433962 24.528302 37.735849  1.886792 24.528302 20.754717
    ## [22]  7.547170 22.641509  1.886792 11.320755 18.867925  3.773585 11.320755
    ## [29] 13.207547  9.433962  9.433962  9.433962  1.886792  1.886792  1.886792
    ## [36]  9.433962 41.509434  7.547170  3.773585 41.509434  0.000000  7.547170
    ## [43]  7.547170  7.547170  7.547170  3.773585 41.509434 45.283019 11.320755
    ## [50] 11.320755 11.320755  7.547170  1.886792  1.886792  5.660377 16.981132
    ## [57]  3.773585 26.415094  0.000000  5.660377 11.320755 11.320755 11.320755
    ## [64]  0.000000  0.000000 11.320755 43.396226 11.320755 81.132075  3.773585
    ## [71]  1.886792 11.320755  7.547170 11.320755 22.641509 77.358491 47.169811
    ## [78]  3.773585  5.660377  5.660377  1.886792  1.886792  1.886792  3.773585
    ## [85]  7.547170  7.547170  5.660377 41.509434 22.641509 22.641509 18.867925
    ## [92]  9.433962 18.867925  7.547170  1.886792

Temos então 0.6736842 de linhas com mais de 5% de NA. Temos então 0.4210526 de linhas com mais de 10% de NA. Temos então 0.2842105 de linhas com mais de 15% de NA.

Aqui temos um plot simples com o histograma das colunas com maior número de dados faltantes. Também temos uma ordenacão das mesmas para facilitar a compreensão delas.

``` r
library(VIM)
aggr_plot <- aggr(x_data, col=c('navyblue','red'), numbers=TRUE, sortVars=TRUE, labels=names(x_data), cex.axis=.7, gap=3, ylab=c("Histogram of missing data","Pattern"))
```

![](YPDS_files/figure-markdown_github/unnamed-chunk-9-1.png)

    ## 
    ##  Variables sorted by number of missings: 
    ##           Variable      Count
    ##             lysine 0.63157895
    ##       acidtolerant 0.53684211
    ##         X40cgrowth 0.52631579
    ##            xylitol 0.46315789
    ##         cadaverine 0.45263158
    ##  vitaminfreegrowth 0.44210526
    ##    cyclohex1000ppm 0.35789474
    ##        glucosamine 0.28421053
    ##           methanol 0.28421053
    ##     gluconolactone 0.27368421
    ##  X50.glucosegrowth 0.25263158
    ##     ureaseactivity 0.25263158
    ##  X60.glucosegrowth 0.24210526
    ##         citricacid 0.24210526
    ##         galactitol 0.14736842
    ##       amdglucoside 0.13684211
    ##     acidproduction 0.12631579
    ##            ethanol 0.12631579
    ##         X37cgrowth 0.11578947
    ##     cyclohex100ppm 0.11578947
    ##         lacticacid 0.11578947
    ##       succinicacid 0.11578947
    ##   starchproduction 0.09473684
    ##           inositol 0.08421053
    ##          lipolytic 0.08421053
    ##           rhamnose 0.08421053
    ##      solublestarch 0.08421053
    ##            ribitol 0.07368421
    ##         ethylamine 0.06315789
    ##           glycerol 0.06315789
    ##         larabinose 0.06315789
    ##          raffinose 0.06315789
    ##             ribose 0.06315789
    ##            sorbose 0.06315789
    ##             inulin 0.05263158
    ##            nh42so4 0.05263158
    ##         darabinose 0.04210526
    ##         erythritol 0.04210526
    ##          melibiose 0.04210526
    ##         melizitose 0.04210526
    ##           sorbitol 0.04210526
    ##          trehalose 0.04210526
    ##             xylose 0.04210526
    ##           mannitol 0.03157895
    ##  arbutinhydrolysis 0.02105263
    ##               kno3 0.02105263
    ##         cellobiose 0.01052632
    ##            lactose 0.01052632
    ##            maltose 0.01052632
    ##            salicin 0.01052632
    ##            sucrose 0.01052632
    ##          galactose 0.00000000
    ##            glucose 0.00000000
