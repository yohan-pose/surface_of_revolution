def plan_tangent(T):
  ## Definition de la courbe generatrice gamma=(x,0,z) sur I=[smin,smax]
  x(s)=#...
  z(s)=#...
  smin,smax = #...,...
  ## Definition de la parametrisation de notre surface de revolution
  f(s,theta) = (x(s)*cos(theta),
                x(s)*sin(theta),
                z(s))
  ## Definition des f's et f't
  dfs(s,theta) = ((x.derivative(s))(s)*cos(theta),
                  (x.derivative(s))(s)*sin(theta),
                  (z.derivative(s))(s))
  
  dft(s,theta) = (-x(s)*sin(theta),
                  x(s)*cos(theta),
                  0)
  ## P.S. : Je dérive "à la main" f car j'ai un problème avec SageMaths lorsqu'il dérive des fonctions trigonométriques à n-var. surement dû à mon instalation, d'après le forum...
  N(s,theta) = (-(z.derivative(s))(s)*x(s)*cos(theta),
                -(z.derivative(s))(s)*x(s)*sin(theta),
                (x.derivative(s))(s)*x(s))
  n(s,theta) = -N(s,theta)/N.norm()
  ## Construction de notre support dependant du temps T
  M = parametric_plot3d(f(s,theta), (s, smin, smax),(theta,0,2*pi),texture='red',alpha=0.75)
  ## Construction de notre plan tangent et de notre normal dependant du temps T
  TM = parametric_plot3d(s*dfs(pi/2,t)+theta*dft(pi/2,t)+f(pi/2,t),(s,-smax/2, smax/2),(theta,-smax/2, smax/2),color='orange',alpha=0.5)
  NM = arrow3d(f(pi/2,t),f(pi/2,t)+n(pi/2,t), color='green',alpha=0.5)
  return M+Ox+Oy+Oz+TM+NM
## On construit ensuite notre animation,
frames = [plan_tangent(T) for T in (0.01, pi/32, pi/16, .., 2*pi)]
plot = animate(frames).interactive()
