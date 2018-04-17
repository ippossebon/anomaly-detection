set terminal x11
set xtics ("Voting" 0.25, "AdaBoost" 1.75, "Bagging" 3.25, "Stacking" 4.75, "SVM" 6.25, "KNN" 7.75, "Decision Tree" 9.25)

set boxwidth 0.5
set style fill solid

set title "Accuracy results"
set grid
plot [-1:11] [0.7:1.05] 'acc.dat' every 2    using 1:2 with boxes lc rgb 'blue' title "Artificial data",\
     'acc.dat' every 2::1 using 1:2 with boxes lc rgb 'red' title "Real data"

set terminal png font "Helvetica"
set output 'accuracy.png'

replot
