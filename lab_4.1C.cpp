#include <iostream>
#include <algorithm>
#include <cmath>

int main() {
    double S, v, h, u, t;

    std::cout << "Enter S (distance), v (taxi speed), h (taxi cost per km), u (walking speed), t (time): ";
    std::cin >> S >> v >> h >> u >> t;

    // Option 1: Taxi for the entire distance
    double taxi_time = S / v;
    double taxi_cost = S * h;
    double min_cost = std::numeric_limits<double>::max();

    if (taxi_time <= t) {
        min_cost = std::min(min_cost, taxi_cost);
    }

    // Option 2: Walking + Taxi
    double min_cost_combination = std::numeric_limits<double>::max();
    double min_cost_pure_walking = std::numeric_limits<double>::max();
    
    if (u > 0) {
        double walking_time = S / u;
        if (walking_time <= t) {
            min_cost_pure_walking = 0;
        }

        // Try different x values to minimize cost
        for (double x = 0; x <= S; x += 0.01) {
            double taxi_time_comb = x / v;
            double walking_time_comb = (S - x) / u;
            if (taxi_time_comb + walking_time_comb <= t) {
                double cost_comb = x * h;
                min_cost_combination = std::min(min_cost_combination, cost_comb);
            }
        }
    }

    min_cost = std::min({min_cost, min_cost_combination, min_cost_pure_walking});
    
    if (min_cost == std::numeric_limits<double>::max()) {
        std::cout << "It's not possible to reach within the given time." << std::endl;
    } else {
        std::cout << "Minimum cost: " << min_cost << " UAH" << std::endl;
    }

    return 0;
}
