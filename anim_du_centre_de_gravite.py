def centre_de_grav(T):
  smax = #...
  smin = #...
  
  x(s) = #...
  y(s) = #...
  z(s) = #...
  
  dx(s) = x.derivative(s)(s)
  dy(s) = y.derivative(s)(s)
  dz(s) = z.derivative(s)(s)
  
  xGt=integral(x*sqrt(dx^2+dy^2+dz^2)/integral(sqrt(dx^2+dy^2+dz^2),(s,smin,smax)),(s,smin,smax))
  yGt=integral(y*sqrt(dx^2+dy^2+dz^2)/integral(sqrt(dx^2+dy^2+dz^2),(s,smin,smax)),(s,smin,smax))
  zGt=integral(z*sqrt(dx^2+dy^2+dz^2)/integral(sqrt(dx^2+dy^2+dz^2),(s,smin,smax)),(s,smin,smax))
  
  xG(u)=integral(x*sqrt(dx^2+dy^2+dz^2)/integral(sqrt(dx^2+dy^2+dz^2),(s,-u,u)),(s,-u,u))
  yG(u)=integral(y*sqrt(dx^2+dy^2+dz^2)/integral(sqrt(dx^2+dy^2+dz^2),(s,-u,u)),(s,-u,u))
  zG(u)=integral(z*sqrt(dx^2+dy^2+dz^2)/integral(sqrt(dx^2+dy^2+dz^2),(s,-u,u)),(s,-u,u))
  
  gammatot = parametric_plot3d((x,y,z), (s, smin, smax), color='black')
  gamma = parametric_plot3d((x,y,z), (s,-t, t), color='green',thickness=4)
  dottot = point3d((xGt,yGt,zGt),size=10,color='blue')
  dot = point3d((xG(t),yG(t),zG(t)),size=10,color='orange')
  return gammatot+gamma+dot+dottot

frames = [centre_de_grav(T) for T in (0.01, smax/32, smax/16, .., smax)]
plot = animate(frames).interactive()
show(plot,frame=false, delay=10, auto_play=False, projection='orthographic')
