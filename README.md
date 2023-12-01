# Initialise the project structure

## Windows
```shell
for (($i = 1); $i -lt 26; $i++) {
  New-Item -ItemType Directory -Path "./day_${i}";
  New-Item -ItemType File -Path "./day_${i}/Problem_${i}.md"
}
```