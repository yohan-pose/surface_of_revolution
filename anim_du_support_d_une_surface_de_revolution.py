# SageMaths >10.4 
def support_de_Sigma(T):
   ## Definition de la courbe generatrice gamma=(x,0,z) sur I=[smin,smax]
   x(s) = #...
   z(s) = #...
   smin,smax = #...,...
   ## Definition de la parametrisation de notre surface de revolution
   f(s,theta) = (x(s)*cos(theta),
                 x(s)*sin(theta),
                 z(s))
   ## Construction de notre support dependant du temps T
   M = parametric_plot3d(f(s,theta), (s, smin, smax),(theta,0,T),texture='red',alpha=0.75)
   ## Construction de nos axes (optionnel)
   Ox = parametric_plot3d((s,0,0), (s, smin-1/4, smax+1/4),color='black')
   Oy = parametric_plot3d((0,s,0), (s, smin-1/4, smax+1/4),color='black')
   Oz = parametric_plot3d((0,0,s), (s, smin-1/4, smax+1/4),color='black')
   
   return M+Ox+Oy+Oz

## On construit ensuite notre animation,
frames = [support_de_Sigma(T) for T in (0.01, pi/32, pi/16, .., 2*pi)]
plot = animate(frames).interactive()
## On affiche l'animation avec un "retard" de 7
show(plot,frame=false, delay=7, auto_play=False, projection='orthographic')
