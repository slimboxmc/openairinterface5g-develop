df -h

apt-get clean

apt-get update
apt-get install -y gnupg2 ca-certificates ubuntu-keyring
apt-get update




apt install git -y


ls

git clone https://github.com/slimboxmc/openairinterface5g-develop.git
cd openairinterface5g-develop/cmake_targets
ls
chmod +x build_oai
sudo apt install cmake -y
cmake --version
./build_oai -I --nrUE --gNB
#./build_oai  -w USRP --ninja --nrUE --gNB --build-lib "nrscope" -C

cd ran_build
#ls
cd build


cp nr-softmodem /opt/oai-gnb/bin/nr-softmodem
cp nr-uesoftmodem /opt/oai-gnb/bin/nr-uesoftmodem


echo "Press [CTRL+C] to stop..."
while true
do
    
    sleep 2
done
#/home/tonic/CCW/openairinterface5g-develop/cmake_targets/ran_build/build_nr_ue_rach_less
#docker cp rfsim5g-oai-cu_b:/opt/oai-gnb/bin/nr-softmodem /home/tonic/CCW/openairinterface5g-develop/cmake_targets/ran_build/build_rach_less/nr-softmodem
#docker cp rfsim5g-oai-cu_b:/opt/oai-gnb/bin/nr-uesoftmodem /home/tonic/CCW/openairinterface5g-develop/cmake_targets/ran_build/build_nr_ue_rach_less/nr-uesoftmodem

#docker exec rfsim5g-oai-cu_b cp /opt/oai-gnb/bin/nr-softmodem /home/tonic/CCW/openairinterface5g-develop/cmake_targets/ran_build/build_rach_less/nr-softmodem
#docker exec rfsim5g-oai-cu_b cp /opt/oai-gnb/bin/nr-uesoftmodem /home/tonic/CCW/openairinterface5g-develop/cmake_targets/ran_build/build_nr_ue_rach_less/nr-uesoftmodem

#docker ls rfsim5g-oai-cu_b:/opt/oai-gnb/bin/nr-softmodem 
#docker exec -it rfsim5g-oai-cu_b /bin/sh

#docker cp  /home/tonic/CCW/openairinterface5g-develop/cmake_targets/ran_build/build_rach_less/nr-softmodem rfsim5g-oai-cu:/opt/oai-gnb/bin/nr-softmodem 
# docker cp rfsim5g-oai-cu_b:/opt/oai-gnb/ /home/tonic/CCW/openairinterface5g-develop/cmake_targets/ran_build/build_rach_less/

