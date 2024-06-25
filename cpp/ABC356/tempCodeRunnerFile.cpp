
    // auto m2{cnt2(M)};

    // vector<bool> bM{};
    // for (int i=0; i<m2+1; i++) {
    //     if (M>>i & 1) {
    //         bM.emplace_back(true);
    //     }
    // }

    // vl fact2{1};
    // for (int i=0; i<m2+1; i++) {
    //     fact2.emplace_back(fact2.back() * 2 % mod);
    // }

    // vl accum{0};
    // for (int i=0; i<m2+1; i++) {
    //     ll s{0LL};
    //     for (const auto& f : fact2) {
    //         s += f;
    //         s %= mod;
    //     }
    //     if (bM[i]) {
    //         accum.emplace_back((accum.back() * 2 + 1) % mod);
    //     } else {
    //         accum.emplace_back((accum.back() * 2) % mod);
    //     }
    // }

    // ll ans{0LL};
    // auto n2{cnt2(N)};
    // for (int i=0; i<n2; i++) {
    //     if (N>>i & 1) {
    //         ans += accum[i] + 1;
    //     }
    // }

    // cout << ans;