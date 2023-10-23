#include <stdio.h>
#include <stdbool.h>
struct coord {
    int x;
    int y;
};

int main() {
    int n;
    scanf("%d", &n);
    struct coord res[n*n];
    

    return 0;
}

bool is_legal(struct coord path, int n, int x, int y){
    int i;
    for(i=0; i<sizeof(*path); i++){
        if((path[i].x == x && path[i].y==y) || !(0<=x<n) || !(0<=y<n)){
            return false;
        };
    };
    return true;
}