(define (problem bluesense) (:domain covisstorage)

(:objects 
  rgbsensebluep motoract1p )

(:init 

  (rgbsenseblue rgbsensebluep)
  (motoract1 motoract1p)
  )
  
(:goal (actuate1 motoract1p))

)