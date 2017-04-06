#!/bin/sh
echo "**********************************"
echo "*****        K-MEANS         *****"
echo "**********************************"
echo " "
for n_cluster in $(seq 2 10); do
	python kmeans.py $n_cluster;
done


echo "**********************************"
echo "***     MINI BATCH K-MEANS     ***"
echo "**********************************"
echo " "
for n_cluster in $(seq 2 10); do
	python minibatch.py $n_cluster;
done

echo "**********************************"
echo "*****           HAC          *****"
echo "**********************************"
echo " "
for n_cluster in $(seq 2 10); do
	python hac.py $n_cluster;
done