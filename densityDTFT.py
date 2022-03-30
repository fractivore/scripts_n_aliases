import numpy
import matplotlib.pyplot as plt

def main():
    set_selected = [1,3,9,27]
    dtft = natural_density_dtft(set_selected)
    dtft.plot_frequency_spectrum()

class natural_density_dtft:

    def __init__(self, set_of_naturals):
        self.this_set = numpy.array(set_of_naturals)

    def amplitude_of_omega(self,omega):
        """This function returns the amplitude of the frequency component
        at omega for the DTFT of a set of naturals."""
        
        #Calculate the component in frequency omega by summing
        #the appropriate exponentials, just e^-i*omega*k in this case
        return sum(numpy.exp(-1j*omega*self.this_set))

    def plot_frequency_spectrum(self):
        x_axis = numpy.linspace(-100,100,1000)
        y_axis = [self.amplitude_of_omega(omega) for omega in x_axis]
        fix, ax = plt.subplots()
        ax.plot(x_axis,numpy.absolute(y_axis))
        plt.show

if __name__ == "__main__":
    main()
