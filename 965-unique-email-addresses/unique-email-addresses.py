class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        hashSet = set()
        for e in emails:
            local, domain = e.split('@')
            local = local.split('+')[0]
            local = local.replace('.', '')
            hashSet.add((local, domain))
        return len(hashSet)
