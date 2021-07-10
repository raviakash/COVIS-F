(define (problem greensense) (:domain covisstorage)

(:objects 
  rgbsensegreenp motoract2p )

(:init 

  (rgbsensegreen rgbsensegreenp)
  (motoract2 motoract2p)
  )
  
(:goal (actuate2 motoract2p))

)