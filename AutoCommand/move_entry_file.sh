#!/bin/bash
mkdir ../cmake_targets/ran_build/build_nr_ue_rach_less
cp ../cmake_targets/ran_build/build/nr-uesoftmodem ../cmake_targets/ran_build/build_nr_ue_rach_less/nr-uesoftmodem 
cp ../ci-scripts/conf_rach_less/build_nr_ue/entrypoint.sh ../cmake_targets/ran_build/build_nr_ue_rach_less/entrypoint.sh
chmod +x ../cmake_targets/ran_build/build_nr_ue_rach_less/entrypoint.sh
chmod 777 ../cmake_targets/ran_build/build_nr_ue_rach_less/entrypoint.sh


mkdir ../cmake_targets/ran_build/build_rach_less
cp ../cmake_targets/ran_build/build/nr-softmodem ../cmake_targets/ran_build/build_rach_less/nr-softmodem 
cp ../ci-scripts/conf_rach_less/entrypoint.sh ../cmake_targets/ran_build/build_rach_less/entrypoint.sh
chmod +x ../cmake_targets/ran_build/build_rach_less/entrypoint.sh
chmod 777 ../cmake_targets/ran_build/build_rach_less/entrypoint.sh

#docker cp rfsim5g-oai-cu_b:/opt/oai-gnb/bin/nr-softmodem ../../cmake_targets/ran_build/build_rach_less/nr-softmodem

#docker cp rfsim5g-oai-cu_b:/opt/oai-gnb/ /home/tonic/CCW/openairinterface5g-develop/cmake_targets/ran_build/build_rach_less/

#docker cp rfsim5g-oai-cu_b:/opt/oai-gnb/ /home/tonic/CCW/openairinterface5g-develop/cmake_targets/ran_build/build_rach_less/oai-gnb/


c