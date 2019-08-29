import os
import json
import time
import random
from datetime import datetime

def conv2json():
    train = {}
    train["info"] = {"description": "MobilTech Dataset",
            "version": "1.0",
            "year": "2019",
            "date_created": "2019/7/18"}
    train["licenses"] = []
    train["images"] = []
    train["annotations"] = []
    train["categories"] = []

    val = {}
    val["info"] = {"description": "MobilTech Dataset",
            "version": "1.0",
            "year": "2019",
            "date_created": "2019/7/18"}
    val["licenses"] = []
    val["images"] = []
    val["annotations"] = []
    val["categories"] = []


    width = 1920
    height = 1200
    j = 0

    for file in os.listdir("./"):
        if file.endswith(".jpg"):

            ctime = datetime.fromtimestamp(os.stat(file).st_mtime)
            image_dict = {}
            image_dict["file_name"] = file
            image_dict["height"] = height
            image_dict["width"] = width
            image_dict["date_captured"] = str(ctime).split('.')[0]
            image_dict["id"] = int(file.split('.')[0])
            train["images"].append(image_dict)

        if file.endswith(".txt"):

            f = open(file,'r')
            lines = f.readlines()

            for i, line in enumerate(lines):
                ann_dict = {}
                chunk = line.split(' ')

                cx = float(chunk[1])*width
                cy = float(chunk[2])*height
                w = float(chunk[3])*width
                h = float(chunk[4])*height

                tlx = round(cx - w/2, 2)
                tly = round(cy - h/2, 2)

                ann_dict["image_id"] = int(f.name.split('.')[0])
                ann_dict["bbox"] = [tlx,tly,w,h]
                ann_dict["category_id"] = int(chunk[0])
                ann_dict["id"] = i+j+1
                train["annotations"].append(ann_dict)
            f.close()
            j += i+1

    mobiltech_categories_name = [
            'Slow','Stop','yield','noStopping','noParking','noGoingStraight',
            'noRightTurn','noLeftTurn','noUTurn','speedLimit60','speedLimit50',
            'Rotary','AheadOnly','TurnRight','TurnLeft','goStraightOrRight',
            'goStraightOrLeft','UTurn','CrosswalkSign','ChildrenSign','OnewayRight',
            'OnewayLeft','OnewayStraight','yieldToOncomingTraffic','railroadCrossing',
            'signalFlag','Crosswalk_yellow','ChildrenSign_yellow','bicycle','tunnel',
            'bridge','slipperyRoad','roughRoad','speedBump','otherCautionarySigns',
            'noThoroughfare','noCar','noFreightCar','noVan','noMotorcycle',
            'noMotorcycleAndCar','noCultivator','noBicycle','noEntry','noOutstripping',
            'weightLimit','carHeightLimit','carWidthLimit','securingDistancebtwCar',
            'lowestSpeedLimit','noPedestrianWalking','noDangerousGoodsVehicle',
            'otherProhibitedSigns','TurnLeftorUTurn','TurnRightorLeft','TwowayTraffic',
            'RightSidePass','LeftSidePass','PassageClassification','Bypass',
            'PedestrianOnlyRoad','ElderlyCareSign','ProtectionOfTheDisabled','OtherIndicators',
            'Vehicle','TrafficLight']

    for _id, name in enumerate(mobiltech_categories_name):
        cat_dict = {}
        cat_dict["supercategory"] = "sign" if _id < 64 \
                                    else "vehicle" if _id == 64 \
                                    else "trafficlight"
        cat_dict["id"] = _id
        cat_dict["name"] = name
        train["categories"].append(cat_dict)
        val["categories"].append(cat_dict)

    val["images"] = random.sample(train["images"], 2072)
    train["images"] = [ _dict for _dict in train["images"] if _dict not in val["images"]]

    for imgs in val["images"]:
        idx = imgs["id"]
        for ann in train["annotations"]:
            if idx == ann["image_id"]:
                val["annotations"].append(ann)
                train["annotations"].remove(ann)

    with open("instances_mobiltech_train2019.json", 'w') as fp:
        json.dump(train, fp)
    fp.close()

    with open("instances_mobiltech_val2019.json", 'w') as fp:
        json.dump(val, fp)
    fp.close()

    with open("validation_dataset_list.txt", "w") as fp:
        for imgs in val["images"]:
            fp.write("mv {}.jpg {}.txt ../mobiltech_val2019\n".format(imgs["file_name"].split('.')[0], imgs["file_name"].split('.')[0]))
    fp.close()


if __name__ == "__main__":
    conv2json()
