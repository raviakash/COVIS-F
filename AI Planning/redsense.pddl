(define (problem redsense) (:domain covisstorage)

(:objects 
  rgbsenseredp motoract4p )

(:init 

  (rgbsensered rgbsenseredp)
  (motoract4 motoract4p)
  )
  
(:goal (actuate4 motoract4p))

)