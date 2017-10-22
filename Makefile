CXXFLAGS=-DRPI

all: ReceiveRF SendRF

ReceiveRF: 
	$(CXX) $(CXXFLAGS) $(LDFLAGS) $@.c -o $@ -lwiringPi
	
SendRF:
	$(CXX) $(CXXFLAGS) $(LDFLAGS) $@.c -o $@ -lwiringPi
	
clean:
	$(RM) ReceiveRF, SendRF
