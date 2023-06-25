import re
class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        ipv4 = '.' in queryIP
        ipv6 = ':' in queryIP
        if(ipv4 and ipv6):
            return "Neither"
        try:
            if (ipv4):
                octets = queryIP.split('.')
                if(len(octets) != 4):
                    return 'Neither'
                for octet in octets:
                    if(len(octet) > 1 and octet[0] == '0'):
                        return 'Neither'
                    if(not (len(octet))):
                        return 'Neither'
                    octet = int(octet)
                    if (not (0 <= octet <= 255)):
                        return "Neither"
                return "IPv4"
            elif (ipv6):
                regex = re.compile(r'[0-9A-Fa-f]*')
                octets = queryIP.split(':')
                if(len(octets)!=8):
                    return "Neither"
                for octet in octets:
                    if(octet == '' or len(octet) > 4):
                        return "Neither"
                    if(octet == '0'):
                        continue
                    if (len(regex.search(octet).group()) != len(octet)):
                        return "Neither"
                return "IPv6"
            else:
                return "Neither"
        except:
            return "Neither"
solution = Solution()
# print(solution.validIPAddress("2001:0db8:85a3::8A2E:037j:7334"))
# print(solution.validIPAddress("2001:0db8:85a3:0:0:8A2E:0370:7334"))
# print(solution.validIPAddress("2001:0db8:85a3:033:0:8A2E:0370:7334"))
print(solution.validIPAddress("20EE:Fb8:85a3:0:0:8A2E:0370:7334:12"))