from PySipebiMiniValidationBase import PySipebiMiniValidationBase

# An example of Sipebi Mini validation script
# All Sipebi Mini validation script must be derived from PySipebiMiniValidationBase
class PySipebiMiniExample_Val(PySipebiMiniValidationBase):
    # Additional properties which are not in the base class
    isInputFileAvailable = False
    commonMistakeFound = False
    specialMistakeFound = False

    # Values of base class properties requiring different default values
    scriptName = 'PySipebiMiniExample.py'
    sipebiErrorCodes = ['KH01', 'KH02', 'Sipebi Error 1']

    # Supposing there is no override needed in the setup, init_changing_vars, and write_to_file methods
    # We will only need to override execute method as shown below
    def execute(self):
        # Some initialization here
        # re-initialize all the variables (to clear the results from the previous call)
        self.init_changing_vars()

        self.isInputFileAvailable = False
        self.commonMistakeFound = False
        self.specialMistakeFound = False

        # Wrap the whole mechanism except for write_to_file in a single try-except block
        try:
            # Some setup and checking here (i.e. the checking and getting of input files)
            # Supposing the input file cannot be found for some reason
            if not self.isInputFileAvailable:
                self.failReason = 'the input fail is not found'
                return  # Return immediately as nothing else can be done if there is no input file

            # Some validation code here

            # Suppose common mistake(s) is(are) found
            if self.commonMistakeFound:
                # Add the common mistake(s) to the list
                self.commonMistakes.add('diagnostics index [1] [berhari hari] is not generated by [' + self.scriptName + ']')
                self.commonMistakes.add('[IsAmbiguous] value for diagnostics index [2] [Kurukuru, -> kuru-kuru,] is [False]. Excpected: [True]')

            # Suppose special mistake(s) is(are) found
            if self.specialMistakeFound:
                # Add the special mistake(s) to the list
                self.specialMistakes.add('special comments for special mistakes here')

            # Check the conditions to consider that the validation result is 'pass' or 'fail'
            self.isPassed = len(self.commonMistakes) == 0 and len(self.specialMistakes) == 0

            # If we reach this point, the validation has been executed successfully
            # Mark the execution as completed successfully, emptied out all mistakes for the next call
            self.isCompleted = True

        except Exception as e:  # catch essentially all exceptions, NOT the best practice but is sufficient for an example
            self.isCompleted = False
            self.failReason = 'Exception: ' + str(e.args)

        # Write the validation result to a text file using default (base) method
        self.write_to_file()

