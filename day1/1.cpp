#include <bits/stdc++.h>

#define all(a) a.begin(), a.end()
#define pb push_back
#define eb emplace_back
#define sz(a) (int) a.size()
#define bitcount(a) (int) __builtin_popcount(a)
#define bitcountll(a) (int) __builtin_popcountll(a)
#define rep(i, from, to) for (int i = from; i < (to); ++i)

using namespace std;

typedef long long int ll;
typedef long double ld;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef pair<double, double> pdd;
typedef vector<int> vi;

const int N = (int) 1e5 + 10;

void solve1() {
    int x, y;
    vi a, b;
    while (cin >> x >> y) {
      a.pb(x);
      b.pb(y);
    }
    sort(all(a));
    sort(all(b));
    int ans = 0;
    for (int i = 0; i < sz(a); ++i) {
      ans += abs(a[i] - b[i]);
    }
    cout << ans << endl;
}

void solve2() {
    int x, y;
    vi a;
    map<int, int> b;
    while (cin >> x >> y) {
      a.pb(x);
      b[y]++;
    }
    ll ans = 0;
    for (int i : a) {
      ans += 1LL * i * b[i];
    }
    cout << ans << endl;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.precision(20);
    cout << fixed;
    // solve1();
    solve2();
    cout.flush();
    return 0;
}