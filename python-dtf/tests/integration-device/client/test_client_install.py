# Android Device Testing Framework ("dtf")
# Copyright 2013-2016 Jake Valletta (@jake_valletta)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
"""Integration tests for the "client install" utility"""

import dtf.testutils as testutils


class ClientInstallTests(testutils.BasicIntegrationDeviceTest):

    """Wraper for integration tests"""

    def test_install(self):

        """Do an install"""

        rtn = self.run_cmd("client install")
        assert(rtn.return_code == 0)
