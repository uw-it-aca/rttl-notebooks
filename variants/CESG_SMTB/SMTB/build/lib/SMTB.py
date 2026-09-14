# The Structural Mechanics Tool Belt (SMTB) Module
# By Richard Wiebe

# This module imports packages, objects, functions (e.g., pi, trig functions) that I found I used very commonly.
# It also creates a few animated plot functions. These functions are mostly just translation between my preferred syntax to Matplotlib's
# It also creates a consistent notation, and avoids any clashing by mostly importing only the needed functions, not entire libraries.
# This is a raw .py file, an can be imported as a module by any Python file or Notebook.

# GENERAL IMPORTS
#--------------------------------------------------------------------------------------------------------------------------
# Numerical Mathematical Functions & Constants
from math import exp,log,log10,sqrt,asin,acos,atan,atan2,sin,cos,tan,asinh,acosh,atanh,sinh,cosh,tanh,pi,factorial,floor,ceil

# Symbolic Mathematical Functions & Constants. All use post-script s. These give perfect results, i.e., sin_s(pi_s) == 0.
from sympy import exp as exp_s 
from sympy import log as log_s
from sympy import sqrt as sqrt_s
from sympy import asin as asin_s
from sympy import acos as acos_s
from sympy import atan as atan_s
from sympy import atan2 as atan2_s
from sympy import sin as sin_s
from sympy import cos as cos_s
from sympy import tan as tan_s
from sympy import asinh as asinh_s
from sympy import acosh as acosh_s
from sympy import atanh as atanh_s
from sympy import sinh as sinh_s
from sympy import cosh as cosh_s
from sympy import tanh as tanh_s
from sympy import pi as pi_s
from sympy import factorial as factorial_s
from sympy import Matrix as matrix_s
from sympy import lambdify, Lambda

# Numberical Analysis Tools
from numpy.linalg import inv, norm
from numpy import array, zeros, eye, outer, dot, linspace, ones, cross
from numpy import ix_ as list_slice                # Takes list as row & column number, i.e., K(list_slice(rowlist,collist))
from numpy import concatenate as join              # Mathematica syntax
from numpy.linalg import inv
import numpy as np                                 # end up needing large parts of this, just import the whole thing
from scipy.integrate import odeint
from scipy.optimize import fsolve   # Simple root finder.


# Symbolic Analysis Tools
from sympy import dsolve as odesolve
from sympy import diff, integrate, simplify, symbols, collect, Eq
from sympy import Function as symbols_func
from IPython.display import display, Math

# Plotting tools. Note that spb uses sympy, which uses matplotlib. But spb produces nice looking plots and has list plots too for numerical
from spb import plot                            #2D plot of one variable (curves)
from spb import plot_parametric                 #2D parametric curve plots
from spb import plot_implicit                   #2D implicit plots
from spb import plot_parametric_region          #2D implicit region (sympy does this with implicit)
from spb import plot_contour                    #2D Contour plots of 3D function
from spb import plot_polar                      #Cool, sympy doesn't have this explicitly, though it can do it and other coords.
from spb import plot_list                       #This is effectively a list line 2D plot. Not symbolic, but can be combined with them
from spb import plot_vector                     #2D & 3D Vector fields
from spb import plot3d                          #3D plot of two variables (surfaces)
from spb import plot3d_parametric_surface      #3D parametric surface plot
from spb import plot3d_spherical               #3D surface
from spb import plot3d_implicit                #3D iso-surfaces of function of 3 variables
from spb import plot3d_list                    #This is effectively a list line 3D plot. Not symbolic, but can be combined with them
from spb import plot3d_parametric_line as plot3d_parametric                  #3D parametric curve plot
from spb import plotgrid
from matplotlib.pyplot import close as close_fig
from matplotlib.pyplot import get_fignums, show

# Interactive tools for plots
from ipywidgets import interact, interactive, FloatSlider

# END GENERAL IMPORTS
#------------------------------------------------------------------------------------------------------------------------


#------------------------------------------------------------------------------------------------------------------------
# tic, toc function. This will not handle nested cases. 
# Adapted from a Guest user on StackExchange. 

from time import time, sleep

def tic():
    global startTime_for_tictoc
    startTime_for_tictoc = time()

def toc():
    if 'startTime_for_tictoc' in globals():
        print("Elapsed time is " + str(time() - startTime_for_tictoc) + " seconds.")
    else:
        print("Toc: start time not set")
#------------------------------------------------------------------------------------------------------------------------


#------------------------------------------------------------------------------------------------------------------------
# Better Matrix Outputs, matrices or vectors work
def MatrixForm(A):
    A = np.asarray(A)
    
    if A.ndim == 1:
        body = " \\\\ ".join(map(str, A))
        latex = f"\\begin{{bmatrix}} {body} \\end{{bmatrix}}"
    elif A.ndim == 2:
        body = " \\\\ ".join([" & ".join(map(str, row)) for row in A])
        latex = f"\\begin{{bmatrix}} {body} \\end{{bmatrix}}"
    else:
        raise ValueError("MatrixForm supports only 1D or 2D arrays.")
    
    display(Math(latex))
#------------------------------------------------------------------------------------------------------------------------



#------------------------------------------------------------------------------------------------------------------------
# Animated plot functions (Homemade), including some imports that are used only here
from matplotlib.widgets import Slider
from matplotlib.pyplot import subplots as mpl_subplots
from matplotlib.pyplot import figure as mpl_figure
from matplotlib.pyplot import subplots_adjust as mpl_subplots_adjust
from matplotlib.pyplot import axes as mpl_axes
from matplotlib import get_backend


#PLOT ANIMATE

def plot_animate(*args,slider_pars,numpts=50,bot_space=0.25,title=None,xlim=None,ylim=None,**kwargs):
    
    # Get parameter names, ranges, and starting value for each
    par_names=list(slider_pars.keys())  
    par_ranges=list(slider_pars.values())
    par_vals=[];
    for curr_par in par_ranges:
        par_vals.append( (curr_par[0]+curr_par[1])/2 )    

    # Create lambdified functions
    funcs=[];
    xvecs=[];
    plotpars=[];
    for arg in args:
        funcs.append(lambdify((arg[1][0], *par_names), arg[0], modules='numpy'))
        xvecs.append(linspace(arg[1][1],arg[1][2],numpts))
        plotpars.append(arg[2] if len(arg)>2 else {})

    # Create initial plot
    fig, ax = mpl_subplots()
    ax.grid(visible=True, color='gray', linewidth=0.5)
    mpl_subplots_adjust(bottom=bot_space)
    lines=[];
    for i,func in enumerate(funcs):
        yvec = funcs[i](xvecs[i],*par_vals)*ones(numpts) if isinstance(funcs[i](xvecs[i],*par_vals), (int, float)) else funcs[i](xvecs[i],*par_vals)
        line_curr, = ax.plot(xvecs[i], yvec, label="#"+str(i+1), **plotpars[i])
        lines.append(line_curr)
    if xlim:
        ax.set_xlim(xlim[0],xlim[1])
    if ylim:
        ax.set_ylim(ylim[0],ylim[1])
    if title:
        ax.set_title(title)
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')
    ax.legend()

    # Create sliders
    sliders=[]
    for i,curr_par in enumerate(par_ranges):
        ax_slider=mpl_axes([0.1, bot_space-0.12-0.05*i, 0.65, 0.03])   #Slider location. Won't work with too many sliders
        sliders.append(Slider(ax_slider,par_names[i], *curr_par, valinit=par_vals[i]))

    # Update function for sliders
    def update(val):
        for i,slider in enumerate(sliders):
            par_vals[i]=slider.val
        for i,line in enumerate(lines):
            yvec = funcs[i](xvecs[i],*par_vals)*ones(numpts) if isinstance(funcs[i](xvecs[i],*par_vals), (int, float)) else funcs[i](xvecs[i],*par_vals)
            line.set_ydata(yvec)
        if get_backend()=="qtagg":
            fig.canvas.draw()
        elif get_backend()=="widget":
            fig.canvas.draw_idle()
        else:
            fig.canvas.draw()
            
       
    # Attach the update function to the sliders
    for slider in sliders:
        slider.on_changed(update)

    # Finally, show the plot
    show()
    if get_backend()=="qtagg":
        fig.canvas.draw()
    elif get_backend()=="widget":
        fig.canvas.draw_idle()
    else:
        fig.canvas.draw()
        print("You are using the "+ get_backend() + " backend which is not a supported by this plotter, your results may vary")






# PARAMETRIC PLOT ANIMATE

def plot_parametric_animate(*args,slider_pars,numpts=50,bot_space=0.25,title=None,xlim=None,ylim=None,**kwargs):
    
    # Get parameter names, ranges, and starting value for each
    par_names=list(slider_pars.keys())  
    par_ranges=list(slider_pars.values())
    par_vals=[];
    for curr_par in par_ranges:
        par_vals.append( (curr_par[0]+curr_par[1])/2 )    

    # Create lambdified functions
    funcsx=[];
    funcsy=[];
    tvecs=[];
    plotpars=[];
    for arg in args:
        funcsx.append(lambdify((arg[2][0], *par_names), arg[0], modules='numpy'))
        funcsy.append(lambdify((arg[2][0], *par_names), arg[1], modules='numpy'))
        tvecs.append(linspace(arg[2][1],arg[2][2],numpts))
        plotpars.append(arg[3] if len(arg)>3 else {})


    # Create initial plot
    fig, ax = mpl_subplots()
    ax.grid(visible=True, color='gray', linewidth=0.5)
    mpl_subplots_adjust(bottom=bot_space)

       
    lines=[];
    for i,_ in enumerate(funcsx):
        xvec = funcsx[i](tvecs[i],*par_vals)*ones(numpts) if isinstance(funcsx[i](tvecs[i],*par_vals), (int, float)) else funcsx[i](tvecs[i],*par_vals)
        yvec = funcsy[i](tvecs[i],*par_vals)*ones(numpts) if isinstance(funcsy[i](tvecs[i],*par_vals), (int, float)) else funcsy[i](tvecs[i],*par_vals)
        line_curr, = ax.plot(xvec, yvec, label="#"+str(i+1), **plotpars[i])
        lines.append(line_curr)
    if xlim:
        ax.set_xlim(xlim[0],xlim[1])
    if ylim:
        ax.set_ylim(ylim[0],ylim[1])
    if title:
        ax.set_title(title)
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')
    ax.legend()

    # Create sliders
    sliders=[]
    for i,curr_par in enumerate(par_ranges):
        ax_slider=mpl_axes([0.1, bot_space-0.12-0.05*i, 0.65, 0.03])   #Slider location. Won't work with too many sliders
        sliders.append(Slider(ax_slider,par_names[i], *curr_par, valinit=par_vals[i]))

    # Update function for sliders
    def update(val):
        for i,slider in enumerate(sliders):
            par_vals[i]=slider.val
        for i,line in enumerate(lines):
            xvec = funcsx[i](tvecs[i],*par_vals)*ones(numpts) if isinstance(funcsx[i](tvecs[i],*par_vals), (int, float)) else funcsx[i](tvecs[i],*par_vals)
            yvec = funcsy[i](tvecs[i],*par_vals)*ones(numpts) if isinstance(funcsy[i](tvecs[i],*par_vals), (int, float)) else funcsy[i](tvecs[i],*par_vals)
            line.set_xdata(xvec)
            line.set_ydata(yvec)
        if get_backend()=="qtagg":
            fig.canvas.draw()
        elif get_backend()=="widget":
            fig.canvas.draw_idle()
        else:
            fig.canvas.draw()
            
       
    # Attach the update function to the sliders
    for slider in sliders:
        slider.on_changed(update)

    # Finally, show the plot
    show()
    if get_backend()=="qtagg":
        fig.canvas.draw()
    elif get_backend()=="widget":
        fig.canvas.draw_idle()
    else:
        fig.canvas.draw()
        print("You are using the "+ get_backend() + " backend which is not a supported by this plotter, your results may vary")







# 3D PARAMETRIC PLOT ANIMATE

def plot3d_parametric_animate(*args,slider_pars,numpts=50,bot_space=0.25,title=None,xlim=None,ylim=None,zlim=None,**kwargs):
    
    # Get parameter names, ranges, and starting value for each
    par_names=list(slider_pars.keys())  
    par_ranges=list(slider_pars.values())
    par_vals=[];
    for curr_par in par_ranges:
        par_vals.append( (curr_par[0]+curr_par[1])/2 )    

    # Create lambdified functions and the parametric variable range
    funcsx=[];
    funcsy=[];
    funcsz=[];
    tvecs=[];
    plotpars=[];
    for arg in args:
        funcsx.append(lambdify((arg[3][0], *par_names), arg[0], modules='numpy'))
        funcsy.append(lambdify((arg[3][0], *par_names), arg[1], modules='numpy'))
        funcsz.append(lambdify((arg[3][0], *par_names), arg[2], modules='numpy'))
        tvecs.append(linspace(arg[3][1],arg[3][2],numpts))
        plotpars.append(arg[4] if len(arg)>4 else {})


    # Create initial plot
    fig, ax = mpl_subplots(subplot_kw={'projection': '3d'})
    ax.grid(visible=True, color='gray', linewidth=0.5)
    
    #fig, ax = mpl_subplots(111,projection='3d')
    mpl_subplots_adjust(bottom=bot_space)
    lines=[];
    for i,_ in enumerate(funcsx):
        xvec = funcsx[i](tvecs[i],*par_vals)*ones(numpts) if isinstance(funcsx[i](tvecs[i],*par_vals), (int, float)) else funcsx[i](tvecs[i],*par_vals)
        yvec = funcsy[i](tvecs[i],*par_vals)*ones(numpts) if isinstance(funcsy[i](tvecs[i],*par_vals), (int, float)) else funcsy[i](tvecs[i],*par_vals)
        zvec = funcsz[i](tvecs[i],*par_vals)*ones(numpts) if isinstance(funcsz[i](tvecs[i],*par_vals), (int, float)) else funcsz[i](tvecs[i],*par_vals) 
        line_curr, = ax.plot(xvec, yvec, zvec, label="#"+str(i+1), **plotpars[i])
        lines.append(line_curr)
    if xlim:
        ax.set_xlim(xlim[0],xlim[1])
    if ylim:
        ax.set_ylim(ylim[0],ylim[1])
    if zlim:
        ax.set_zlim(zlim[0],zlim[1])
    if title:
        ax.set_title(title)
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')
    ax.legend()

    # Create sliders
    sliders=[]
    for i,curr_par in enumerate(par_ranges):
        ax_slider=mpl_axes([0.1, bot_space-0.12-0.05*i, 0.65, 0.03])   #Slider location. Won't work with too many sliders
        sliders.append(Slider(ax_slider,par_names[i], *curr_par, valinit=par_vals[i]))

    # Update function for sliders
    def update(val):
        for i,slider in enumerate(sliders):
            par_vals[i]=slider.val
        for i,line in enumerate(lines):
            xvec = funcsx[i](tvecs[i],*par_vals)*ones(numpts) if isinstance(funcsx[i](tvecs[i],*par_vals), (int, float)) else funcsx[i](tvecs[i],*par_vals)
            yvec = funcsy[i](tvecs[i],*par_vals)*ones(numpts) if isinstance(funcsy[i](tvecs[i],*par_vals), (int, float)) else funcsy[i](tvecs[i],*par_vals)
            zvec = funcsz[i](tvecs[i],*par_vals)*ones(numpts) if isinstance(funcsz[i](tvecs[i],*par_vals), (int, float)) else funcsz[i](tvecs[i],*par_vals)         
            line.set_data_3d(xvec, yvec,  zvec)
        if get_backend()=="qtagg":
            fig.canvas.draw()
        elif get_backend()=="widget":
            fig.canvas.draw_idle()
        else:
            fig.canvas.draw()
            
       
    # Attach the update function to the sliders
    for slider in sliders:
        slider.on_changed(update)

    # Finally, show the plot
    show()
    if get_backend()=="qtagg":
        fig.canvas.draw()
    elif get_backend()=="widget":
        fig.canvas.draw_idle()
    else:
        fig.canvas.draw()
        print("You are using the "+ get_backend() + " backend which is not a supported by this plotter, your results may vary")








# STACKED ANIMATED PLOTS (Can only do stack/column geometry)
def plot_animate_stack(*args,slider_pars,numpts=50,bot_space=0.25,title=None,xlim=None,ylim=None,**kwargs):
    
    # Get parameter names, ranges, and starting value for each
    par_names=list(slider_pars.keys())  
    par_ranges=list(slider_pars.values())
    par_vals=[]
    for curr_par in par_ranges:
        par_vals.append( (curr_par[0]+curr_par[1])/2 )    

    # Determine number of plots
    nplot = len(args)

    # Create lambdified functions
    funcs=[[] for _ in range(nplot)];
    xvecs=[[] for _ in range(nplot)];
    plotpars=[[] for _ in range(nplot)];
    for j,currplot in enumerate(args):
        if isinstance(currplot[0], tuple):
            for arg in currplot:
                funcs[j].append(lambdify((arg[1][0], *par_names), arg[0], modules='numpy'))
                xvecs[j].append(linspace(arg[1][1],arg[1][2],numpts))
                plotpars[j].append(arg[2] if len(arg)>2 else {})          
        else:
            funcs[j].append(lambdify((currplot[1][0], *par_names), currplot[0], modules='numpy'))
            xvecs[j].append(linspace(currplot[1][1],currplot[1][2],numpts))
            plotpars[j].append(currplot[2] if len(currplot)>2 else {})  


    # Create initial plot
    fig, ax = mpl_subplots(nplot,1)
    for i in range(nplot):
        ax[i].grid(visible=True, color='gray', linewidth=0.5)
        mpl_subplots_adjust(bottom=bot_space)

    lines=[[] for _ in range(nplot)];
    for j,currfunc in enumerate(funcs):
        for i,func in enumerate(currfunc):
            yvec = funcs[j][i](xvecs[j][i],*par_vals)*ones(numpts) if isinstance(funcs[j][i](xvecs[j][i],*par_vals), (int, float)) else funcs[j][i](xvecs[j][i],*par_vals)
            line_curr, = ax[j].plot(xvecs[j][i], yvec, **plotpars[j][i])
            lines[j].append(line_curr)
        if xlim:
            ax[j].set_xlim(xlim[j][0],xlim[j][1])
        if ylim:
            ax[j].set_ylim(ylim[j][0],ylim[j][1])
        if title:
            ax[j].set_title(title[j])
        ax[j].legend()

    # Create sliders
    sliders=[]
    for i,curr_par in enumerate(par_ranges):
        ax_slider=mpl_axes([0.1, bot_space-0.12-0.05*i, 0.65, 0.03])   #Slider location. Won't work with too many sliders
        sliders.append(Slider(ax_slider,par_names[i], *curr_par, valinit=par_vals[i]))

    # Update function for sliders
    def update(val):
        for i,slider in enumerate(sliders):
            par_vals[i]=slider.val
        for j,currline in enumerate(lines):
            for i,line in enumerate(currline):
                yvec = funcs[j][i](xvecs[j][i],*par_vals)*ones(numpts) if isinstance(funcs[j][i](xvecs[j][i],*par_vals), (int, float)) else funcs[j][i](xvecs[j][i],*par_vals)
                lines[j][i].set_ydata(yvec)
        if get_backend()=="qtagg":
            fig.canvas.draw()
        elif get_backend()=="widget":
            fig.canvas.draw_idle()
        else:
            fig.canvas.draw()

    # Attach the update function to the sliders
    for slider in sliders:
        slider.on_changed(update)

    # Finally, show the plot
    show()
    if get_backend()=="qtagg":
        fig.canvas.draw()
    elif get_backend()=="widget":
        fig.canvas.draw_idle()
    else:
        fig.canvas.draw()
        print("You are using the "+ get_backend() + " backend which is not a supported by this plotter, your results may vary")


#------------------------------------------------------------------------------------------------------------------------

        
"""
# REMOVED LIBRARIES. 
# The following were removed as it was just too many plotting options. Simplied to just using spb.

# Numerical Plotting. Just importing the entire matplotlib plotting toolbox, as it works with all sympy stuff too.
import matplotlib.pyplot as plt  

# Standard/Sympy Symbolic Plotting
from sympy.plotting import plot as plot_s                            #2D plot of one variable (curves)
from sympy.plotting import plot_parametric as plot_parametric_s      #2D parametric curve plots
from sympy.plotting import plot_implicit as plot_implicit_s          #2D implicit plots + region (and I think contour can be done with this)
from sympy.plotting import plot3d as plot3d_s                        #3D plot of two variables (surface)
from sympy.plotting import plot3d_parametric_line as plot3d_parametric_s          #3D parametric curve plot
from sympy.plotting import plot3d_parametric_surface as plot3d_parametric_surface_s  #3D parametric surface plot
""";