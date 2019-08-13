# File to modify
./src/lib/opts.py (search for "modify here")

# demo

python demo.py ctdet --demo /path/to/imagefolder --load_model ../models/MODEL_NAME_HERE.pth


# train 
# If the training is terminated before finishing, you can use the same commond with 
# --resume to resume training. It will found the lastest model with the same exp_id.

python main.py ctdet --exp_id mobiltech_dla --batch_size 32 --master_batch 15 --lr 1.25e-4  --gpus 0,1
