
    for (int i=0; i<N; i++) {
        int p;
        cin >> p;
        P.emplace_back(p);
        pos[p] = i;
    }

    set<int> s;
    for (int i=1; i<K; i++) {
        s.insert(pos[i]);
    }

    for (int i=K; i<=N; i++) {
        s.insert(pos[i]);
        ans1 = min(ans1, *s.rbegin() - *s.begin());
        s.erase(pos[i-K+1]);
    }