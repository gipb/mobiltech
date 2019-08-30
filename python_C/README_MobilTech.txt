conda environment : onnx_practice

CenterNet_objdet2D/src/lib/opts.py 에서 
--demo 옵션에 이미지 폴더 경로 (test image가 들어있는 폴더 경로),
--load_model 옵션에 model 경로(model_xxx.pth 까지 설정해야함.)  설정.

command 창에 다음과 같은 명령어를 이용하면 실행 가능.

PYTHONPATH=.:~/practice/CenterNet_objdet2D/src/lib ./run_demo demo demo ctdet
