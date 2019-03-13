#include <iostream>
using namespace std; // consider removing this line in serious projects

int value(int a, int b){
	int max = 0;
	for(int i = a; i <= b; i++){
		int n = i;
		int cont = 1;
		while(n>1){
			if(n%2==1){
				n = (n*3)+1;
			}else{
				n = n/2;
			}
			cont++;
		}
		if (cont > max){
			max = cont;
		}
	}
	
	return max;	
}


int main() {
	int a = 0;
	int b = 0;
	int out = 0;
	while(cin >> a >> b){
		if(a>=b){
			out = value(b,a);	
		}else{
			out = value(a,b);
		}
		cout << a << " " << b << " " << out << endl;
	}
	return 0;
}

