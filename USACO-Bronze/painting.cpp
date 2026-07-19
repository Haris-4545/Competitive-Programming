#include <iostream>
#include <algorithm>

int main() {
    freopen("paint.in", "r", stdin);
    freopen("paint.out", "w", stdout);

    int a, b, c, d;
    std::cin >> a >> b >> c >> d;

    int total_length = (b - a) + (d - c);
    int overlap = std::max(0, std::min(b, d) - std::max(a, c));
    std::cout << total_length - overlap << std::endl;
    return 0;
}