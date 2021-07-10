(define(domain covisstorage)
     (:predicates
         (rgbsenseblue ?rgb1)
         (colordetectblue ?rgb1)
         (motoract1 ?motor1)
         (actuate1 ?motor1)
         (rgbsensegreen ?rgb2)
         (colordetectgreen ?rgb2)
         (motoract2 ?motor2)
         (actuate2 ?motor2)
         (rgbsensered ?rgb3)
         (colordetectred ?rgb3)
         (motoract4 ?motor4)
         (actuate4 ?motor4)
         (pir1 ?pir1)
         (motion1 ?pir1)
         (light1 ?light1)
         (lightglow1 ?light1)
         (temp ?temp1)
         (tempdetect ?temp1)
         (motoract3 ?motor3)
         (actuate3 ?motor3)
         (infra1 ?infra1)
         (infradetect ?infra1)
         (lightr ?light2)
         (lightglowr ?light2)
         (lightg ?light3)
         (lightglowg ?light3)
         )
     
     (:action RGBsensor_blue
       :parameters (?rgb1)
       :precondition (and (rgbsenseblue ?rgb1)(not (colordetectblue ?rgb1)))
       :effect (colordetectblue ?rgb1))
     
     (:action RGBsensor_green
       :parameters (?rgb2)
       :precondition (and (rgbsensegreen ?rgb2)(not (colordetectgreen ?rgb2)))
       :effect (colordetectgreen ?rgb2))
       
     (:action RGBsensor_red
       :parameters (?rgb3)
       :precondition (and (rgbsensered ?rgb3)(not (colordetectred ?rgb3)))
       :effect (colordetectred ?rgb3)) 
       
     (:action Motion_sense
       :parameters (?pir1)
       :precondition (and (pir1 ?pir1) (not(motion1 ?pir1)))
       :effect (motion1 ?pir1))  
      
      (:action Temperature_sense
        :parameters (?temp1)
        :precondition (and (temp ?temp1) (not(tempdetect ?temp1)))
        :effect (tempdetect ?temp1))
        
      (:action Infrared_sense
        :parameters (?infra1)
        :precondition (and (infra1 ?infra1) (not(infradetect ?infra1)))
        :effect (infradetect ?infra1))
        
      (:action Motor1_actuate
        :parameters (?motor1 ?rgb1)
        :precondition (and (motoract1 ?motor1) (not (actuate1 ?motor1)) (or (rgbsenseblue ?rgb1) (colordetectblue ?rgb1)))
        :effect (actuate1 ?motor1))   
        
      (:action Motor2_actuate
        :parameters (?motor2 ?rgb2)
        :precondition (and (motoract2 ?motor2) (not (actuate2 ?motor2)) (or (rgbsensegreen ?rgb2) (colordetectgreen ?rgb2)))
        :effect (actuate2 ?motor2)) 
        
      (:action Motor4_actuate
        :parameters (?motor4 ?rgb3)
        :precondition (and (motoract4 ?motor4) (not (actuate4 ?motor4)) (or (rgbsensered ?rgb3) (colordetectgreen ?rgb3)))
        :effect (actuate4 ?motor4)) 
        
      (:action Light_glow
        :parameters (?pir1 ?light1)
        :precondition (and (light1 ?light1) (not (lightglow1 ?light1)) (or (pir1 ?pir1) (motion1 ?pir1)))
        :effect (lightglow1 ?light1))  
        
      (:action Fan_actuate
        :parameters (?temp1 ?motor3)
        :precondition (and (motoract3 ?motor3) (not (actuate3 ?motor3)) (or (temp ?temp1) (tempdetect ?temp1)))
        :effect (actuate3 ?motor3)) 
        
        (:action lightred
        :parameters (?infra1 ?light2)
        :precondition (and (lightr ?light2) (not (lightglowr ?light2)))
        :effect (lightglowr ?light2)) 
        
      (:action lightgreen
        :parameters (?infra1 ?light3)
        :precondition (and (lightg ?light3) (not (lightglowg ?light3)))
        :effect (lightglowg ?light3)) 
)   
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        