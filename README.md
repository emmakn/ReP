# ReP
**Re**petative **P**ipettor

## Background
The ReP was created to automate repetative pipetting tasks in a simple and cost-effective way. It utilizes a rack and pinion design to move the pipette's plunger up and down. It can be dialed in and calibrated to aspirate and dispense at any given rate, frequency, and volume. It is intended to be held upright with a ring stand clamp or any other clamped arm to allow for easy maneuverability and adaptability. The ReP is built around an Eppendorf pipette. The DC motor is controlled with a Raspberry Pi Nano and an L298N motor controller. The structure itself is 3D printed from PLA.

## Included
In this repository, I have included:
1. STL files for the 3D prints,
2. wiring and construction guides, and
3. the code for the raspberry pi

## 1. 3D Printing
There are seven total pieces that need to be printed: *axle_extension, clip_side1_c, clip_side2_c, housing, motor_holder, pinion,* and *rack_assembly.* None of the pieces require any special printing instructions. PLA is the recommended material given its structural stability and cost. Support material will be required. 20% infill and 0.2 layer height is adequate.

## 2. Wiring and Construction
The final hardware diagram and orientation of 3D printed parts are shown in Figures 1 and 2, respectively. The following guide will walk through the process of wiring and constructing step by step.

1. Solder pins 16, 18, 20, and 22 onto the Nano.
2. Either hot glue or screw the motor controller and Raspberry Pi Nano onto the *clip_side1_c* such that the corners line up with the protrusions on either side of the part. When attaching, be sure the the Nano is facing such that the SD card is facing up and the USB and HDMI ports are facing out. For the motor controller, the heat sink should be facing down. If gluing, make sure to allow the piece to sit for a minute or so to fully dry.
3. Attach all wires as shown in the hardware diagram in Figure 1. The wires leading to the motor can remain unattached for now.
4. Remove all support material from the 3D printed parts. May need to dremel parts down as necessary depending on printing accuracy.
5. Insert the motor into the *motor_holder* with the axle lined up with the top dove groove.
6. Put the *rack_assembly* into the *housing* and line up the *pinion* inside it as well.
7. Carefully slide the *housing* with the *rack_assembling* and *pinion* into the top dove groove of the *motor_holder*. It is important to line up the flat edge of the pinion with the flat edge of the motor's axle and may take some finessing.
8. Slide *clip_slide1_c* into the bottom groove of the *motor_holder*.
9. Attach the two leads from the motor controller to the two nodes on the motor. Figuring out which wire goes to which node will need to be determined by trial and error. If the wires are connected to the wrong nodes, the motor will simply rotate in the opposite direction. The correct orientation will need to be tested by running the up or down program to ensure it goes the correct direction. If the plunger goes down when the up program is ran, simply switch the wires.
