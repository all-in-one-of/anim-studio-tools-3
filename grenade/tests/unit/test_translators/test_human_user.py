#
# Copyright 2010 Dr D Studios Pty Limited (ACN 127 184 954) (Dr. D Studios), its
# affiliates and/or its licensors.
#

from ..helpers.translators import verify_translate

from grenade.translators.human_user import HumanUserTranslator
from probe.fixtures.mock_shotgun import MockShotgun

class TestHumanUserTranslator(object):
    """
    Nose unit test suite for Grenade HumanUserTranslator.
    
    .. versionadded:: v00_04_00
    """
    def setup(self):
        """
        Set up the unit test suite.
        
        .. versionadded:: v00_04_00
        """
        self.shotgun_data = [{'id':1, 'type':'Group'},
                             {'id':2, 'type':'Project'}]
        
        self.session = MockShotgun(schema=[], data=self.shotgun_data)
        self.translator = HumanUserTranslator(self.session)
    
    def teardown(self):
        """
        Tear down the unit test suite.
        
        .. versionadded:: v00_04_00
        """
        pass
    
    def test_translate(self):
        """
        Test that the translator converts the supplied test data as expected.
        
        .. versionadded:: v00_04_00
        """
        verify_translate(self.translator, 'groups', [{'id':1, 'type':'Group'}], [{'Group':[['id', 'is', 1]]}], [{'Group':[['id', 'is', 2]]}])
        verify_translate(self.translator, 'projects', [{'id':2, 'type':'Project'}], [{'Project':[['id', 'is', 2]]}], [{'Project':[['id', 'is', 3]]}])

# Copyright 2008-2012 Dr D Studios Pty Limited (ACN 127 184 954) (Dr. D Studios)
#
# This file is part of anim-studio-tools.
#
# anim-studio-tools is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# anim-studio-tools is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with anim-studio-tools.  If not, see <http://www.gnu.org/licenses/>.

