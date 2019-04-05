def cost_of_ground_shipping(weight):
  if weight <= 2:
    price_per_lb =  1.50
  elif (weight > 2) and (weight <= 6):
    price_per_lb = 3.00
  elif (weight > 6) and (weight <= 10):
    price_per_lb = 4.00
  else:
    price_per_lb = 4.75
    
  return 20 + (price_per_lb * weight)
    
print(cost_of_ground_shipping(8.4))

shipping_cost_premium = 125.00

def drone_shipping(weight):
  if weight <= 2:
    price_per_lb =  4.50
  elif (weight > 2) and (weight <= 6):
    price_per_lb = 9.00
  elif (weight > 6) and (weight <= 10):
    price_per_lb = 12.00
  else:
    price_per_lb = 14.25
    
  return (price_per_lb * weight)

print(drone_shipping(1.5))

def cheapest_method(weight):
  ground = cost_of_ground_shipping(weight)
  premium = shipping_cost_premium
  drone = drone_shipping(weight)
  
  if ground < premium and ground < drone:
    method = "standard ground"
    cost = ground
  elif premium < ground and premium < drone:
    method = "premium"
    cost = premium
  else:
    method = "drone"
    cost = drone
  print("The cheapest option is %s shipping at $%.2f." % (method, cost))

print(cheapest_method(4.8))
print(cheapest_method(41.5))
