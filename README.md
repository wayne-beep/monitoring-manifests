# Thanos Manifests

This repository provides [Kustomize][1] base to deploy [Prometheus][2] +
[Thanos][3] + [n9e][4] and example overlays for general deployment in
 kubernetes cluster.

## Usage

To use the base, reference the remote in you `kustomization.yaml`

```
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization
resources:
  - github.com:wayne-beep/thanos-manifests.git
```

You MUST provide the following ConfigMaps:

- `prometheus`
- `thanos-storage`
- `thanos-query`
- `n9e-server`
- `n9e-webapi`

### Additional Components

You will find that the base actually pulls each individual component as a sub-
base. The reason for this is so that we can add additional components without
having to deploy the entire stack.

The prime example of this is adding an extra set of a `prometheus`,
`thanos-storage` and `thanos-compact` stack which can be used with a separate
configuration. You can reference the more specific bases:

## Requires

- https://github.com/kubernetes-sigs/kustomize

```
go get -u sigs.k8s.io/kustomize
```

[1]: https://kustomize.io/
[2]: https://prometheus.io/
[3]: https://thanos.io/
[4]: https://n9e.github.io
