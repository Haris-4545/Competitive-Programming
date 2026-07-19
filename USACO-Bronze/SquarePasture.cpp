#include <iostream>
#include <cstdio>
#include <algorithm>

int main() {
    freopen("square.in", "r", stdin);
    freopen("square.out", "w", stdout);

    int x1, y1, x2, y2;
    int x3, y3, x4, y4;

    std::cin >> x1 >> y1 >> x2 >> y2;
    std::cin >> x3 >> y3 >> x4 >> y4;

    int min_x = std::min(x1, x3);
    int max_x = std::max(x2, x4);
    int min_y = std::min(y1, y3);
    int max_y = std::max(y2, y4);

    int side_length = std::max(max_x - min_x, max_y - min_y);

    std::cout << side_length * side_length << std::endl;
    return 0;
}