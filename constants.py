# these values are for MS COCO
image_size = 500.0
layer_boxes = [3, 6, 6, 6, 6, 6] 
classes = 80
batch_size = 2
box_ratios = [1.0, 1.0, 2.0, 3.0, 0.5, 1.0/3.0]
conv4_3_ratios = [1.0, 0.5, 2.0]
conv4_3_box_scale = 0.07
box_s_min = 0.1
layer_shapes = None # to be set programmatically
negposratio = 3