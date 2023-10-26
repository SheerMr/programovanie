#include <stdio.h>
#include <stdbool.h>
struct coord {
    int x;
    int y;
};
struct moves {
    struct coord pohyby[8];
};

bool is_legal(struct coord path[], int n, int x, int y){
    int i;
    for(i=0; i<n*n; i++){
        if((path[i].x == x && path[i].y==y) || x>=n || x<0|| y<0||y>=n){
            return false;
        };
    };
    return true;
}

struct moves find_moves(int n, struct coord path[], int x, int y){
    struct moves out;
    int i;
    for(i=0; i<8; i++){
        out.pohyby[i].x = -1;
        out.pohyby[i].y = -1;
    }
    struct coord cycle[] = {{2, 1}, {-2, 1}, {2, -1}, {-2, -1},
     {1, 2}, {1, -2}, {-1, 2}, {-1, -2}};
    int k = 0;
    for(i=0; i<8; i++){
        if(is_legal(path, n, x+cycle[i].x, y+cycle[i].y)){
            out.pohyby[k].x = x+cycle[i].x;
            out.pohyby[k].y = y+cycle[i].y;
            k++;
        };
    };
    return out;
}
void solve(struct coord path[], int n, int depth){
    int i, j;
    if(depth==n*n-1){
        for(i=0; i<n*n;i++){
            if(i==0){
                printf("[");
            }
            else{printf(" ");}
            printf("%d %d,", path[i].x, path[i].y);
        }
        printf("]\n");
        return;
    }
    struct moves pohyby = find_moves(n, path, path[depth].x, path[depth].y);
    struct coord newpath[n*n];
    for(j=0; j<n*n; j++){
        newpath[j].x = path[j].x;
        newpath[j].y = path[j].y;
    }
    for(i=0; i<8; i++){
        if(pohyby.pohyby[i].x ==-1){
            break;
        }

        newpath[depth+1].x = pohyby.pohyby[i].x;
        newpath[depth+1].y = pohyby.pohyby[i].y;
        solve(newpath, n, depth+1);
    }

}

int main() {
    int n;
    scanf("%d", &n);
    struct coord res[n*n];
    int i;
    for(i=0; i<n*n; i++){
        res[i].x = -1;
        res[i].y = -1;
    }
    res[0].x = 0;
    res[0].y = 0;
    solve(res, n, 0);

    return 0;
}