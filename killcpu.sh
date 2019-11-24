#! /bin/sh  
# filename killcpu.sh 
#--------------------------------------------
#消耗CPU资源，如果服务器是有多颗CPU，可以选择消耗多少颗CPU的资源
#参数3表示消耗3颗CPU的资源 ./killcpu.sh 3
#--------------------------------------------

if [ $# != 1 ] ; then 
  echo "USAGE: $0 <CPUs>"
  exit 1; 
fi
for i in `seq $1` 
do
  echo -ne "  
i=0;  
while true 
do 
i=i+1;  
done" | /bin/sh & 
  pid_array[$i]=$! ; 
done

for i in "${pid_array[@]}"; do
  echo 'kill ' $i ';'; 
done
