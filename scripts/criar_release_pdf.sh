#!/usr/bin/env bash
set -euo pipefail

remote="${REMOTE:-origin}"
branch="$(git branch --show-current)"

if [ -z "$branch" ]; then
  echo "Nao foi possivel identificar a branch atual."
  exit 1
fi

if [ -n "$(git status --porcelain)" ]; then
  echo "A arvore de trabalho possui alteracoes pendentes. Faca commit antes de criar o release."
  exit 1
fi

command -v gh >/dev/null 2>&1 || {
  echo "GitHub CLI (gh) nao encontrado."
  exit 1
}

git fetch --tags "$remote"

if [ "${1:-}" ]; then
  tag="$1"
  fail_on_collision=1
else
  base_tag="release-$(date +%Y-%m-%d-%H%M)"
  tag="$base_tag"
  fail_on_collision=0
fi

tag_exists() {
  git rev-parse -q --verify "refs/tags/$1" >/dev/null || \
    git ls-remote --exit-code --tags "$remote" "refs/tags/$1" >/dev/null 2>&1 || \
    gh release view "$1" >/dev/null 2>&1
}

suffix=2
while tag_exists "$tag"; do
  if [ "$fail_on_collision" -eq 1 ]; then
    echo "A tag ou release $tag ja existe. Use um nome novo."
    exit 1
  fi

  tag="${base_tag}-${suffix}"
  suffix=$((suffix + 1))
done

title="Release ${tag#release-}"
notes="PDF gerado e anexado automaticamente pelo workflow Build PDF."

git push "$remote" "$branch"
git tag -a "$tag" -m "$title"
git push "$remote" "$tag"
gh release create "$tag" --title "$title" --notes "$notes"

echo "Release criado: $tag"
