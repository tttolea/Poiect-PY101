#include <stdio.h>

#define N 5

int matr[N][N] = {
    {0, 1, 1, 0, 0},
    {1, 0, 0, 1, 1},
    {1, 0, 0, 0, 1},
    {0, 1, 0, 0, 0},
    {0, 1, 1, 0, 0}};

int vzt[N];

void DFS(int nod)
{
    printf("%d ", nod + 1);
    vzt[nod] = 1;
    for (int i = 0; i < N; i++)
    {
        if (matr[nod][i] && !vzt[i])
        {
            DFS(i);
        }
    }
}
//tesssst
void bfs(int start)
{
    int queue[N], front = 0, rear = 0;
    vzt[start] = 1;
    queue[rear++] = start;
    while (front < rear)
    {
        int nod = queue[front++];
        printf("%d ", nod + 1);
        for (int i = 0; i < N; i++)
        {
            if (matr[nod][i] && !vzt[i])
            {
                vzt[i] = 1;
                queue[rear++] = i;
            }
        }
    }
}

int main()
{
    int matr[N][N] = {
    {0, 1, 1, 0, 0},
    {1, 0, 0, 1, 1},
    {1, 0, 0, 0, 1},
    {0, 1, 0, 0, 0},
    {0, 1, 1, 0, 0}};
    for (int i = 0; i < N; i++)
        vzt[i] = 0;
    DFS(0);

    printf("\n");

    for (int i = 0; i < N; i++)
        vzt[i] = 0;
    bfs(0);

    return 0;
}
