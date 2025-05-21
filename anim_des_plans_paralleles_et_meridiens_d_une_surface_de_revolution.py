def parallel(T):
  ## Definition de la courbe generatrice gamma=(x,0,z) sur I=[smin,smax]
  x(s)=#...
  z(s)=#...
  smin,smax = #...,...
  ## Definition de la parametrisation de notre surface de revolution
  f(s,theta) = (x(s)*cos(theta),
                x(s)*sin(theta),
                z(s))
  ## Construction de notre support dependant du temps T
  M = parametric_plot3d(f(s,theta), (s, smin, smax),(theta,0,2*pi),texture='red',alpha=0.75)
  ## Construction de notre plan parallèle et de notre parallèle dependant du temps T
  P1par = parametric_plot3d((s,theta,t), (s,-smax/2, smax/2),(theta,-smax/2, smax/2), color='orange',alpha=0.5)
  Par = parametric_plot3d(f(t,theta), (theta, 0, 2*pi),color='green',thickness=4)
  ## Construction de notre plan méridien et de notre méridien dependant du temps T
  # P2mer = parametric_plot3d(R(s,0,theta,t), (s,-smax/2, smax/2), (theta,0,pi), color='orange',alpha=0.5)
  # Mer = parametric_plot3d(f(s,t), (s, 0, smax), color='green',thickness=4)
  return M+Ox+Oy+Oz+Par+P1par

## On construit ensuite notre animation,
frames = [parallel(T) for T in (0.01, pi/32, pi/16, .., 2*pi)]
plot = animate(frames).interactive()

## On affiche l'animation avec un "retard" de 7
show(plot,frame=false, delay=7, auto_play=False, projection='orthographic')
